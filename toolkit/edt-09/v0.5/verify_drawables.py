"""Verify explicitly mapped, byte-preserved PNG drawables in a trusted APK."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import zipfile


def require(ok, message):
    if not ok:
        raise ValueError(message)


def valid_hash(value):
    return isinstance(value, str) and re.fullmatch(r'[0-9a-fA-F]{64}', value)


def verify(path, receipt):
    require(isinstance(receipt, dict) and set(receipt) == {'schema', 'apk_sha256', 'drawables'}, 'Invalid receipt')
    require(type(receipt['schema']) is int and receipt['schema'] == 1, 'Unsupported schema')
    expected = receipt['apk_sha256']
    require(valid_hash(expected), 'Invalid APK hash')
    mappings = receipt['drawables']
    require(isinstance(mappings, dict) and 0 < len(mappings) <= 128, 'Invalid drawable mappings')
    for name, sha in mappings.items():
        require(isinstance(name, str) and re.fullmatch(r'res/drawable(?:-[a-zA-Z0-9]+)*/[a-z0-9_]+\.png', name), 'Expected exact PNG drawable path')
        require(valid_hash(sha), 'Invalid drawable hash')
    with Path(path).open('rb') as stream:
        require(stream.seek(0, 2) <= 512 * 1024 * 1024, 'APK exceeds limit')
        stream.seek(0)
        require(hashlib.file_digest(stream, 'sha256').hexdigest() == expected.lower(), 'APK hash mismatch')
        stream.seek(0)
        with zipfile.ZipFile(stream) as apk:
            entries = apk.infolist()
            names = [e.filename for e in entries]
            require(len(names) <= 50000 and len(names) == len(set(names)), 'Too many or duplicate entries')
            require('AndroidManifest.xml' in names, 'Missing manifest marker')
            for name, sha in mappings.items():
                require(name in names and sum(n.casefold() == name.casefold() for n in names) == 1, 'Missing or ambiguous drawable: ' + name)
                entry = apk.getinfo(name)
                require(entry.orig_filename == name and stat.S_IFMT(entry.external_attr >> 16) in (0, stat.S_IFREG), 'Nonregular drawable')
                require(not entry.flag_bits & 1 and entry.compress_type in (0, 8), 'Unsupported member encoding')
                require(0 < entry.file_size <= 16 * 1024 * 1024, 'Drawable size limit')
                with apk.open(entry) as member:
                    data = member.read(16 * 1024 * 1024 + 1)
                require(len(data) == entry.file_size and hashlib.sha256(data).hexdigest() == sha.lower(), 'Drawable hash mismatch: ' + name)
                require(data.startswith(b'\x89PNG\r\n\x1a\n'), 'Missing PNG signature')
        stream.seek(0)
        require(hashlib.file_digest(stream, 'sha256').hexdigest() == expected.lower(), 'APK changed during inspection')
    return {'status': 'mapped_drawable_bytes_match', 'apk_sha256': expected.lower(), 'drawables': sorted(mappings), 'scope': 'Exact mapped bytes only; no Android resource resolution or signature verification'}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'Duplicate JSON key')
        result[key] = value
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('apk', type=Path)
    p.add_argument('receipt', type=Path)
    a = p.parse_args()
    try:
        print(json.dumps(verify(a.apk, json.loads(a.receipt.read_text(encoding='utf-8'), object_pairs_hook=unique_object)), indent=2))
    except (ValueError, OSError, RuntimeError, zipfile.BadZipFile) as exc:
        p.exit(1, 'Drawable verification failed: ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
