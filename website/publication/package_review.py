"""Build an offline REVIEW ZIP only. Never deploy or package the repository wholesale."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

PINS = {
    "website/prototype/index.html": ("git", "6d74bbe7680d7ac8a2aac167edd54fd0127f3812"),
    "website/prototype/site.css": ("git", "733d6e7c5adf56f74aeaee13b05af2d895b4cc7e"),
    "website/prototype/products/sudoku.html": ("git", "a825e606c7a794dfa09651fba3a63ca76213cc97"),
    "website/prototype/products/word-search.html": ("git", "de07b1e27c1ca0d43ed8f5d9fc1771be36f273b9"),
    "website/prototype/products/grid-hunt.html": ("git", "d9dad075dd9cd0ec8129d16d3cfa94c54653f64b"),
    "website/prototype/products/crossroads.html": ("git", "ea061e2650915ae7e836a3207e4bf7075dc311bc"),
    "website/prototype/products/sector-rebound.html": ("git", "b0771b60fa6f19901f2614769049bbdef0f97615"),
    "website/prototype/products/eden-comms.html": ("git", "807838a9bab6737d597db0035cad01a05f295b4e"),
    "branding/spudacus/v1.0/full-transparent.png": ("sha256", "74773dbda822161f73a639f959e8bce5c6e0b333a94ebeb8ee27f620d4995d25"),
    "branding/gridmates/v1.0/runtime-transparent.png": ("sha256", "eef6d631cac0b9523f7e0dbebac229f9a2458d36fe2e73e111d251704d9ff292"),
    "branding/eps/v1.0/runtime-transparent.png": ("sha256", "d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516"),
}
RECEIPT = "REVIEW-ONLY.json"

def fingerprint(data, mode):
    if mode == "git":
        return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if mode == "sha256":
        return hashlib.sha256(data).hexdigest()
    raise ValueError("unknown fingerprint mode")

def collect(root):
    root = root.resolve()
    files = {}
    for name, (mode, expected) in sorted(PINS.items()):
        p = root / name
        if p.resolve() != p or not p.is_file():
            raise ValueError("missing or redirected input: " + name)
        data = p.read_bytes()
        if fingerprint(data, mode) != expected:
            raise ValueError("unreviewed input change: " + name)
        files[name] = data
    receipt = {"schema": 1, "purpose": "offline review only", "publication_authorized": False,
               "entry": "website/prototype/index.html",
               "files": {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}}
    files[RECEIPT] = (json.dumps(receipt, indent=2, sort_keys=True)+"\n").encode()
    return files

def build(root, output):
    files = collect(root)
    # No overwrite; callers choose a fresh output outside the source tree.
    output = output.absolute()
    if output.parent.resolve() != output.parent or output.suffix != ".zip":
        raise ValueError("output must be a ZIP in a real directory")
    if output.is_relative_to(root.resolve()):
        raise ValueError("output must be outside repository")
    with output.open("xb") as raw:
        try:
            with ZipFile(raw, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
                for name, data in sorted(files.items()):
                    info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                    info.compress_type = ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, data)
            raw.flush()
            with ZipFile(output) as archive:
                if archive.namelist() != sorted(files) or archive.testzip() is not None:
                    raise ValueError("archive inventory or CRC mismatch")
                for name, data in files.items():
                    if archive.read(name) != data:
                        raise ValueError("archive bytes mismatch: " + name)
        except BaseException:
            raw.close()
            output.unlink()
            raise
    return {"purpose": "review only", "publication_authorized": False,
            "entries": len(files), "sha256": hashlib.sha256(output.read_bytes()).hexdigest()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(build(Path(__file__).resolve().parents[2], args.output), indent=2))
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(1, str(exc)+"\n")

if __name__ == "__main__":
    main()
