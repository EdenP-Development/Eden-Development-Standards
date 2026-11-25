"""Verify a ZIP against a trusted external receipt; never extract or modify it."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import zipfile

MAX_ARCHIVE = 64 * 1024 * 1024
MAX_FILE = 16 * 1024 * 1024
MAX_TOTAL = 128 * 1024 * 1024
MAX_FILES = 1024


def require(ok, message):
    if not ok:
        raise ValueError(message)


def valid_name(name):
    return isinstance(name, str) and all(re.fullmatch(r'[A-Za-z0-9_-][A-Za-z0-9_.-]*', p) and not p.endswith('.') and p.split('.')[0].upper() not in {'CON','PRN','AUX','NUL',*(f'COM{i}' for i in range(1,10)),*(f'LPT{i}' for i in range(1,10))} for p in name.split('/'))


def valid_hash(value):
    return isinstance(value, str) and re.fullmatch(r'[0-9a-fA-F]{64}', value)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'Duplicate JSON key')
        result[key] = value
    return result


def verify(path, receipt):
    require(isinstance(receipt, dict) and set(receipt) == {'schema','archive_sha256','files'}, 'Invalid receipt')
    require(type(receipt['schema']) is int and receipt['schema'] == 1, 'Unsupported schema')
    require(valid_hash(receipt['archive_sha256']), 'Invalid archive hash')
    records = receipt['files']
    require(isinstance(records, list) and 0 < len(records) <= MAX_FILES, 'Invalid file count')
    expected = {}
    folded = set()
    for record in records:
        require(isinstance(record, dict) and set(record) == {'path','sha256'}, 'Invalid file record')
        name, digest = record['path'], record['sha256']
        require(valid_name(name) and valid_hash(digest), 'Invalid name or hash')
        require(name.casefold() not in folded, 'Duplicate or case-colliding path')
        folded.add(name.casefold())
        expected[name] = digest.lower()
    for name in folded:
        parts = name.split('/')
        require(not any('/'.join(parts[:i]) in folded for i in range(1,len(parts))), 'File/directory collision')
    with Path(path).open('rb') as stream:
        raw = stream.read(MAX_ARCHIVE + 1)
    require(len(raw) <= MAX_ARCHIVE, 'Archive exceeds size limit')
    require(hashlib.sha256(raw).hexdigest() == receipt['archive_sha256'].lower(), 'Archive hash mismatch')
    import io
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        entries = archive.infolist()
        names = [e.filename for e in entries]
        require(len(entries) == len(expected) and set(names) == set(expected), 'Unexpected, duplicate or missing entry')
        require(sum(e.file_size for e in entries) <= MAX_TOTAL, 'Total size exceeds limit')
        for entry in entries:
            require(entry.orig_filename == entry.filename and not entry.is_dir(), 'Invalid archive entry')
            require(stat.S_IFMT(entry.external_attr >> 16) in (0, stat.S_IFREG), 'Nonregular entry')
            require(not entry.flag_bits & 1 and entry.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED), 'Unsupported encryption or compression')
            require(0 <= entry.file_size <= MAX_FILE, 'Entry exceeds size limit')
            with archive.open(entry) as item:
                data = item.read(MAX_FILE + 1)
            require(len(data) == entry.file_size and len(data) <= MAX_FILE, 'Entry size mismatch')
            require(hashlib.sha256(data).hexdigest() == expected[entry.filename], 'Asset hash mismatch: ' + entry.filename)
    return {'status':'archive_bytes_verified','files':len(expected),'scope':'Archive and listed member bytes only'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('receipt', type=Path)
    args = parser.parse_args()
    try:
        receipt = json.loads(args.receipt.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
        print(json.dumps(verify(args.archive, receipt), indent=2))
    except (ValueError, OSError, zipfile.BadZipFile, RuntimeError) as exc:
        parser.exit(1, 'Asset verification failed: ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
