"""Extract and rebuild the private V8 review shell without changing HTML bytes.
Usage: python modular-shell.py extract INPUT.zip SOURCE_DIR
       python modular-shell.py build SOURCE_DIR OUTPUT_DIR
Local review only; not a publication packager.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

SHELL = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{title}</title><link rel="stylesheet" href="style.css"></head><body{attrs}><a class="skip" href="#main">Skip to content</a>{header}{main}{footer}</body></html>{tail}'
PATTERN = re.compile(r'<title>(?P<title>.*?)</title>.*?<body(?P<attrs>[^>]*)>.*?(?P<header><header>.*?</header>)(?P<main><main.*?</main>)(?P<footer><footer>.*?</footer>)</body></html>(?P<tail>\s*)$', re.S)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def extract(archive, dest):
    with zipfile.ZipFile(archive) as z:
        receipt = json.loads(z.read('receipt.json'))
        assert receipt['publication_authorized'] is False
        assert len(z.namelist()) == len(set(z.namelist()))
        assert set(z.namelist()) == set(receipt['files']) | {'receipt.json'}
        pages = {}
        for name, expected in receipt['files'].items():
            data = z.read(name)
            assert digest(data) == expected, name
            if re.fullmatch(r'[a-z-]+\.html', name):
                match = PATTERN.search(data.decode('utf-8'))
                assert match, name
                fields = match.groupdict()
                assert SHELL.format(**fields).encode() == data, name
                pages[name] = fields
        dest.mkdir(parents=True, exist_ok=False)
        (dest / 'pages.json').write_text(json.dumps(pages, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def build(source, dest):
    pages = json.loads((source / 'pages.json').read_text(encoding='utf-8'))
    dest.mkdir(parents=True, exist_ok=False)
    for name, fields in pages.items():
        if not re.fullmatch(r'[a-z-]+\.html', name):
            raise ValueError('Invalid page filename')
        (dest / name).write_bytes(SHELL.format(**fields).encode('utf-8'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['extract', 'build'])
    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    (extract if args.mode == 'extract' else build)(args.source, args.destination)
