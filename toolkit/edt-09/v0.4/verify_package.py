"""Read-only verification of byte-preserved assets in a trusted local APK."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import zipfile

MAX_PACKAGE = 512 * 1024 * 1024
MAX_MEMBER = 16 * 1024 * 1024
MAX_ENTRIES = 50000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(stream):
    return hashlib.file_digest(stream, 'sha256').hexdigest()


def safe_path(name):
    return isinstance(name, str) and all(re.fullmatch(r'[A-Za-z0-9_-][A-Za-z0-9_.-]*', p) for p in name.split('/'))


def verify(path, receipt):
    require(isinstance(receipt, dict) and set(receipt) == {'schema','apk_sha256','required','exclusive_prefixes'}, 'Invalid receipt fields')
    require(type(receipt['schema']) is int and receipt['schema'] == 1, 'Invalid schema')
    expected_hash = receipt['apk_sha256']
    require(isinstance(expected_hash, str) and re.fullmatch(r'[0-9a-fA-F]{64}', expected_hash), 'Invalid APK hash')
    required = receipt['required']
    require(isinstance(required, dict) and 0 < len(required) <= 1024, 'Invalid required assets')
    for name, sha in required.items():
        require(safe_path(name) and name.startswith('assets/') and isinstance(sha,str) and re.fullmatch(r'[0-9a-fA-F]{64}',sha), 'Invalid asset receipt')
    prefixes = receipt['exclusive_prefixes']
    require(isinstance(prefixes,list) and all(isinstance(p,str) and p.endswith('/') and safe_path(p[:-1]) and p.startswith('assets/') for p in prefixes), 'Invalid exclusive prefixes')
    with Path(path).open('rb') as stream:
        require(stream.seek(0,2) <= MAX_PACKAGE, 'Package too large')
        stream.seek(0)
        require(digest(stream) == expected_hash.lower(), 'APK hash mismatch')
        stream.seek(0)
        with zipfile.ZipFile(stream) as archive:
            entries = archive.infolist()
            require(len(entries) <= MAX_ENTRIES, 'Too many entries')
            names = [e.filename for e in entries]
            require(len(names) == len(set(names)), 'Duplicate ZIP entry')
            require('AndroidManifest.xml' in names, 'Missing Android manifest')
            assets = [n for n in names if n.startswith('assets/')]
            require(len(assets) == len(set(n.casefold() for n in assets)), 'Asset case collision')
            for prefix in prefixes:
                require({n for n in assets if n.casefold().startswith(prefix.casefold())} == {n for n in required if n.startswith(prefix)}, 'Unexpected or missing asset under ' + prefix)
            for name, expected in required.items():
                require(name in names, 'Missing asset: ' + name)
                entry = archive.getinfo(name)
                require(entry.orig_filename == name and not entry.is_dir() and stat.S_IFMT(entry.external_attr >> 16) in (0,stat.S_IFREG), 'Nonregular asset')
                require(not entry.flag_bits & 1 and entry.compress_type in (zipfile.ZIP_STORED,zipfile.ZIP_DEFLATED), 'Unsupported asset compression or encryption')
                require(0 <= entry.file_size <= MAX_MEMBER, 'Asset too large')
                with archive.open(entry) as member:
                    data = member.read(MAX_MEMBER+1)
                require(len(data) == entry.file_size and hashlib.sha256(data).hexdigest() == expected.lower(), 'Asset hash mismatch: ' + name)
        stream.seek(0)
        require(digest(stream) == expected_hash.lower(), 'APK changed during verification')
    return {'status':'packaged_asset_bytes_match','apk_sha256':expected_hash.lower(),'verified_assets':sorted(required),'exclusive_prefixes':prefixes}


def unique_object(pairs):
    result = {}
    for k,v in pairs:
        require(k not in result, 'Duplicate JSON key')
        result[k] = v
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('apk',type=Path); p.add_argument('receipt',type=Path)
    a=p.parse_args()
    try:
        print(json.dumps(verify(a.apk,json.loads(a.receipt.read_text(encoding='utf-8'),object_pairs_hook=unique_object)),indent=2))
    except (ValueError,OSError,zipfile.BadZipFile,RuntimeError) as exc:
        p.exit(1,'Package verification failed: '+str(exc)+'\n')


if __name__ == '__main__':
    main()
