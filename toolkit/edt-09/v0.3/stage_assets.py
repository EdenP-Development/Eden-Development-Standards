"""Stage selected verified images in a new local directory; never overwrite."""
import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import zipfile


def load(name, version, filename):
    path = Path(__file__).resolve().parent.parent / version / filename
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


archive_check = load('edt09_archive', 'v0.1', 'verify_assets.py')
image_check = load('edt09_image', 'v0.2', 'verify_image.py')
require = archive_check.require


def stage(archive, receipt, selection, destination):
    destination = Path(destination)
    require(not destination.exists() and not destination.is_symlink(), 'Destination must not exist')
    require(isinstance(selection, dict) and set(selection) == {'schema', 'images'}, 'Invalid selection')
    require(type(selection['schema']) is int and selection['schema'] == 1, 'Invalid selection schema')
    images = selection['images']
    require(isinstance(images, list) and 0 < len(images) <= archive_check.MAX_FILES, 'Invalid selection count')
    with Path(archive).open('rb') as stream:
        raw = stream.read(archive_check.MAX_ARCHIVE + 1)
    require(len(raw) <= archive_check.MAX_ARCHIVE, 'Archive too large')
    # Both verification and staging use the same captured bytes.
    with tempfile.TemporaryDirectory() as tmp:
        snapshot = Path(tmp) / 'snapshot.zip'
        snapshot.write_bytes(raw)
        archive_check.verify(snapshot, receipt)
    expected = {r['path']: r['sha256'].lower() for r in receipt['files']}
    selected = []
    names, sources = set(), set()
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for item in images:
            require(isinstance(item, dict) and set(item) == {'source','name','format','width','height','alpha','box','color'}, 'Invalid selection record')
            source, name = item['source'], item['name']
            require(isinstance(source, str) and source in expected and source not in sources, 'Unknown or duplicate source')
            require(archive_check.valid_name(name) and '/' not in name, 'Expected flat safe filename')
            require(name.casefold() not in names and name.casefold() != 'manifest.json', 'Duplicate or reserved output')
            require(item['format'] in ('PNG','WEBP') and Path(name).suffix.lower() == '.' + item['format'].lower(), 'Output extension mismatch')
            sources.add(source); names.add(name.casefold())
            data = z.read(source)
            contract = image_check.verify(data, expected[source], item['format'], item['width'], item['height'], item['alpha'], item['box'], item['color'])
            selected.append((name, data, {'path':name,'source':source,'sha256':expected[source],'contract':contract}))
    result = {'schema':1,'status':'staged_not_release_approved','archive_sha256':hashlib.sha256(raw).hexdigest(),'files':[r for _,_,r in selected]}
    # Exclusive creation. Parent must be a trusted existing local directory.
    destination.mkdir(exist_ok=False)
    try:
        for name, data, _ in selected:
            with (destination / name).open('xb') as stream:
                stream.write(data)
        with (destination / 'manifest.json').open('x', encoding='utf-8') as stream:
            json.dump(result, stream, indent=2)
            stream.write('\n')
    except Exception:
        shutil.rmtree(destination)
        raise
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('archive','receipt','selection','destination'):
        p.add_argument(name, type=Path)
    a = p.parse_args()
    try:
        def read(path):
            return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=archive_check.unique_object)
        print(json.dumps(stage(a.archive, read(a.receipt), read(a.selection), a.destination), indent=2))
    except (ValueError, OSError, TypeError, SyntaxError, RuntimeError, zipfile.BadZipFile) as exc:
        p.exit(1, 'Staging failed: ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
