"""Rebuild the pinned private V8 review site; never publish it."""
import argparse
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import subprocess
import sys

PIN = 'a24db7e8e3f2bfe0531591b1a8c088d862e98a3d69b0251bb8bc6e5e30802fcc'
HERE = Path(__file__).resolve().parent

def sha(data):
    return hashlib.sha256(data).hexdigest()

class Page(HTMLParser):
    def __init__(self, data):
        super().__init__()
        self.ids, self.refs = set(), []
        self.feed(data.decode('utf-8'))
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == 'id':
                self.ids.add(value)
            if key in ('href', 'src') and value:
                self.refs.append(value)

def validate(payload):
    pages = {name: Page(data) for name, data in payload.items() if name.endswith('.html')}
    count = 0
    for name, page in pages.items():
        for ref in page.refs:
            u = urlsplit(ref)
            if u.scheme in ('https', 'http') and u.netloc:
                continue
            if u.scheme or u.netloc or u.path.startswith('/'):
                raise ValueError('Unsupported reference: ' + ref)
            target = unquote(u.path) or name
            if target not in payload or (u.fragment and (target not in pages or unquote(u.fragment) not in pages[target].ids)):
                raise ValueError(name + ': broken reference ' + ref)
            count += 1
    return count

def run(archive, output):
    if output.exists():
        raise FileExistsError(output)
    if sha(archive.read_bytes()) != PIN:
        raise ValueError('Unrecognized review archive')
    with zipfile.ZipFile(archive) as z:
        receipt_bytes = z.read('receipt.json')
        receipt = json.loads(receipt_bytes)
        files = receipt['files']
        if receipt['publication_authorized'] is not False or sorted(z.namelist()) != sorted([*files, 'receipt.json']):
            raise ValueError('Invalid receipt or archive entries')
        original = {}
        for name, digest in files.items():
            if not re.fullmatch(r'(?:[a-z-]+\.html|style\.css|assets/[a-zA-Z0-9_.-]+\.(?:png|webp))', name):
                raise ValueError('Unsupported payload path: ' + name)
            data = z.read(name)
            if sha(data) != digest:
                raise ValueError('Hash mismatch: ' + name)
            original[name] = data
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        def call(script, *args):
            subprocess.run([sys.executable, str(HERE / script), *map(str, args)], check=True)
        call('modular-shell.py', 'extract', archive, root / 'source')
        call('catalog.py', 'normalize', root / 'source/pages.json', root / 'catalog.json')
        call('catalog.py', 'expand', root / 'catalog.json', root / 'catalog-pages.json')
        call('navigation.py', 'normalize', root / 'catalog-pages.json', root / 'navigation.json')
        (root / 'expanded').mkdir()
        call('navigation.py', 'expand', root / 'navigation.json', root / 'expanded/pages.json')
        call('modular-shell.py', 'build', root / 'expanded', root / 'html')
        rebuilt = {p.name: p.read_bytes() for p in (root / 'html').glob('*.html')}
        payload = {**{k:v for k,v in original.items() if not k.endswith('.html')}, **rebuilt}
        if payload != original:
            raise ValueError('Exact output parity failed')
        count = validate(payload)
        output.mkdir(parents=True, exist_ok=False)
        for name, data in {**payload, 'receipt.json': receipt_bytes}.items():
            path = output / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        result = {'publication_authorized': False, 'input_sha256': PIN, 'pages': len(rebuilt), 'payloads': len(payload), 'local_html_references': count, 'exact_payload_parity': True}
        print(json.dumps(result, sort_keys=True))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    run(args.archive, args.output)
