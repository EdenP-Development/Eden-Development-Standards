"""EDT-08: read-only verification of independently recorded baseline files."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys


def require(ok, message):
    if not ok:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'Duplicate JSON key: ' + key)
        result[key] = value
    return result


def verify(root, manifest):
    root = Path(root).resolve(strict=True)
    require(root.is_dir(), 'Root must be a directory')
    require(isinstance(manifest, dict) and set(manifest) == {'schema', 'files'}, 'Invalid manifest fields')
    require(type(manifest['schema']) is int and manifest['schema'] == 1, 'Unsupported schema')
    files = manifest['files']
    require(isinstance(files, list) and files, 'Nonempty file list required')
    seen = set()
    receipts = []
    for entry in files:
        require(isinstance(entry, dict) and set(entry) == {'path', 'sha256'}, 'Invalid file record')
        name, expected = entry['path'], entry['sha256']
        require(isinstance(name, str) and name and '\\' not in name and ':' not in name and '\x00' not in name, 'Invalid relative path')
        relative = PurePosixPath(name)
        require(not relative.is_absolute() and all(p not in ('', '.', '..') for p in name.split('/')), 'Unsafe relative path')
        require(name not in seen, 'Duplicate path: ' + name)
        seen.add(name)
        require(isinstance(expected, str) and re.fullmatch(r'[0-9a-fA-F]{64}', expected), 'Invalid SHA256: ' + name)
        path = root
        for part in relative.parts:
            path = path / part
            require(not path.is_symlink(), 'Symbolic link rejected: ' + name)
        require(path.is_file() and path.resolve(strict=True).is_relative_to(root), 'Missing or outside root: ' + name)
        with path.open('rb') as stream:
            actual = hashlib.file_digest(stream, 'sha256').hexdigest()
        require(actual == expected.lower(), 'Hash mismatch: ' + name)
        receipts.append({'path': name, 'sha256': actual})
    return {'status': 'baseline_hashes_match', 'files': receipts, 'scope': 'Listed file bytes only; no runtime or complete tree verification'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--manifest', required=True, type=Path)
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
        print(json.dumps(verify(args.root, manifest), indent=2))
    except (ValueError, OSError) as exc:
        print('Baseline verification failed: ' + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
