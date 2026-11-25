"""Read-only image contract checks; use trusted local files and receipts."""
import argparse
import hashlib
import io
import json
from pathlib import Path
from PIL import Image

MAX_BYTES = 16 * 1024 * 1024
MAX_PIXELS = 16_000_000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def verify(data, expected_hash, fmt, width, height, alpha='any', box=None, color=None):
    require(len(data) <= MAX_BYTES, 'Image byte limit exceeded')
    require(hashlib.sha256(data).hexdigest() == expected_hash.lower(), 'Image hash mismatch')
    require(fmt in ('PNG', 'WEBP'), 'Unsupported format contract')
    require(type(width) is int and type(height) is int and width > 0 and height > 0 and width * height <= MAX_PIXELS, 'Invalid dimensions')
    require(alpha in ('any', 'opaque', 'transparent'), 'Invalid alpha contract')
    with Image.open(io.BytesIO(data), formats=[fmt]) as im:
        require(im.format == fmt and im.size == (width, height), 'Format or dimensions mismatch')
        require(getattr(im, 'n_frames', 1) == 1, 'Animated image unsupported')
        im.verify()
    with Image.open(io.BytesIO(data), formats=[fmt]) as im:
        im.load()
        rgba = im.convert('RGBA')
        a = rgba.getchannel('A')
        low, high = a.getextrema()
        bounds = a.getbbox()
        if alpha == 'opaque':
            require(low == 255, 'Expected opaque image')
        if alpha == 'transparent':
            require(low == 0 and high > 0, 'Expected transparent pixels and visible art')
        if box is not None:
            require(len(box) == 4 and all(type(n) is int for n in box), 'Invalid box')
            x0, y0, x1, y1 = box
            require(0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height, 'Box outside canvas')
            require(bounds is not None and bounds[0] >= x0 and bounds[1] >= y0 and bounds[2] <= x1 and bounds[3] <= y1, 'Artwork outside allowed box')
        if color is not None:
            require(len(color) == 3 and all(type(n) is int and 0 <= n <= 255 for n in color), 'Invalid RGB color')
            require(all(v == (c, c) for v, c in zip(rgba.getextrema(), (*color, 255))), 'Expected uniform opaque background')
        return {'status': 'image_contract_pass', 'format': fmt, 'size': [width, height], 'alpha_extrema': [low, high], 'visible_bounds': bounds}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('image', type=Path)
    p.add_argument('--sha256', required=True)
    p.add_argument('--format', required=True, choices=['PNG', 'WEBP'])
    p.add_argument('--width', required=True, type=int)
    p.add_argument('--height', required=True, type=int)
    p.add_argument('--alpha', choices=['any','opaque','transparent'], default='any')
    p.add_argument('--box', nargs=4, type=int)
    p.add_argument('--color', nargs=3, type=int)
    args = p.parse_args()
    try:
        with args.image.open('rb') as stream:
            data = stream.read(MAX_BYTES + 1)
        print(json.dumps(verify(data, args.sha256, args.format, args.width, args.height, args.alpha, args.box, args.color), indent=2))
    except (OSError, ValueError, Image.DecompressionBombError) as exc:
        p.exit(1, 'Image verification failed: ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
