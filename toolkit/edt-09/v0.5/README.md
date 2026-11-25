# EDT-09 v0.5 — Explicit byte-preserved drawable verification

2026-11-25. Companion to v0.4, which remains unchanged. Python 3.11+ standard library. Read-only verification of an exact APK against an independently recorded APK SHA-256 and explicit PNG drawable path-to-hash mapping. No installation, extraction, signing or network.

```sh
python -m unittest -q
python -O -m unittest -q
python verify_drawables.py /path/to/GridMates-Sudoku-Beta3-Visual4.apk sudoku-visual4-receipt.json
```

Receipt schema 1: apk_sha256 and drawables object mapping exact res/drawable[-qualifier]/lowercase_name.png member paths to expected SHA256. Only explicitly byte-preserved PNGs; no inference of resource IDs, qualifiers, adaptive icon selection or Android runtime resolution. AAPT2 may transform source assets; a transformed resource requires a separate reviewed contract. PNG signature check is not full image decoding. Reject missing/ambiguous mapped paths, duplicate ZIP entries, invalid hashes, unsupported member encodings and size limits. Use trusted stable local APKs and receipts; not an adversarial filesystem/ZIP sandbox. Unmapped resources are not certified. No signature verification or release approval.

## Executed evidence
Python 3.13.5: 8/8 unit tests passed both normal and optimized. Exact committed blob hashes match local tested source 05654bce17b085529633eca92059b5cb849e5718, tests 6c452b82317cb376582062fbf5db8b931c1db53d, pilot receipt ca3bceeed85f857444ed1cd24f415fd357ae6411.

Real historical Sudoku Beta 3 Visual Review 4 pilot: run 45550962814, artifact 14993249624, source 96747991e98f78c90e10d6eda447d1be085a3674. Downloaded artifact ZIP rehashed to 1a1d26951560641f30d3caa6bef24b633d2c27492eb1235a55815632bc100b07; extracted exact APK SHA256 fa8cf012c1a0fa458da5cc8301e50aa34046a9c964f8bfa51e792ba8906a292a (43,212,096 bytes). Receipt pins independently recorded startup master hashes from branding/game-startup/v1.0/README.md and the recorded build receipt. Executed verifier returned mapped_drawable_bytes_match for both Spudacus and GridMates PNGs. This is real consumer-artifact verification of two mapped resources only, not consumer CI integration, latest-build acceptance, launcher inspection, signature verification or runtime test. Artifact retention is limited; independent owner archive still required. No APK committed.

Next: adopt this check on a focused product QA workflow only when exact current build and independent mapping receipts are available; retain existing resource and runtime acceptance gates. No application code modified.
