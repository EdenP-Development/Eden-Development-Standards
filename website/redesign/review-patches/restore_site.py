"""Restore the exact V14 static review site to a new local directory."""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

PIN = '61666f4365ffd16a02d2ca5508fd5ce6b2a962c58fb829f7e83ca832aefeb0f4'


def restore(archive, destination):
    if destination.exists():
        raise FileExistsError(destination)
    if hashlib.sha256(archive.read_bytes()).hexdigest() != PIN:
        raise ValueError('Unexpected candidate archive')
    with zipfile.ZipFile(archive) as z:
        receipt = json.loads(z.read('receipt.json'))
        files = receipt['files']
        if receipt['publication_authorized'] is not False or sorted(z.namelist()) != sorted([*files, 'receipt.json']):
            raise ValueError('Invalid private candidate')
        payload = {}
        for name, digest in files.items():
            if not re.fullmatch(r'(?:[a-z-]+\.html|style\.css|assets/[a-z0-9_-]+\.(?:png|webp))', name):
                raise ValueError('Unexpected file: ' + name)
            data = z.read(name)
            if hashlib.sha256(data).hexdigest() != digest:
                raise ValueError('Payload mismatch: ' + name)
            payload[name] = data
        if len(payload) != 38 or sum(n.endswith('.html') for n in payload) != 13:
            raise ValueError('Incomplete candidate')
    destination.mkdir(parents=True)
    for name, data in payload.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    print('Restored 38 review files; no publication authorized.')


if __name__ == '__main__':
    restore(Path(sys.argv[1]), Path(sys.argv[2]))
