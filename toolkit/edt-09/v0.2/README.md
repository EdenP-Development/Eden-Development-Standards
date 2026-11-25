# EDT-09 v0.2 — Image contract verifier

2026-11-25. Companion to v0.1 ZIP receipt verification; not an integrated archive extraction or packaging tool. Python 3.11+; Pillow 12.3.0 pinned to locally tested version. Review dependency rights, notices and security updates before adoption.

Read-only checks: independently recorded SHA256, actual PNG/WebP encoding, dimensions, single frame, decoder integrity, alpha extrema, visible alpha bounds, optional allowed rectangle and exact uniform opaque RGB. Maximum 16 MiB input, 16 million expected pixels. Intended for trusted local artwork, not hostile image sandboxing. No output image modifications.

```sh
python -m pip install -r requirements.txt
python -m unittest -v
python -O -m unittest -q
python verify_image.py foreground.png --sha256 EXPECTED_HASH --format PNG --width 432 --height 432 --alpha transparent --box 100 100 332 332
python verify_image.py background.png --sha256 EXPECTED_HASH --format PNG --width 432 --height 432 --alpha opaque --color 33 79 63
```

GridMates examples are derived from branding/gridmates/app-icons/v1.0/README.md: 432px adaptive foreground canvas, nominal centered 232px art box, runtime #214F3F. Box uses exclusive right/bottom coordinates. Containment is not proof of exact footprint, centering, frame thickness or optical consistency. Background command applies only to a raster representation of the color; actual Android XML resource and overrides need separate verification. All actual product icons remain untested here. Do not modify art just to make a check pass; approved optical adjustments require owner review.

12/12 tests passed locally in standard and optimized Python using real Pillow PNG/WebP decoding. Exact committed blobs verified against locally tested bytes: source 8a013df104be451d6cccda9d4f2dc66be6dc874c, tests ff95316694451bb8e20ad288892c22b732e7803b. Synthetic images only. No CI, Android package or consumer acceptance. v0.1 retained. Next controlled staging with independent receipts and explicit runtime selection; no automatic overwrite.
