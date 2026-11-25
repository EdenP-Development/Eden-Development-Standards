# EDT-09 v0.3 — Controlled asset staging

2026-11-25. Integrates the preserved sibling v0.1 archive verifier and v0.2 image verifier. Python 3.11+; install Pillow from ../v0.2/requirements.txt. Keep version directories together. Use only trusted local artwork, receipts, selection and an existing trusted output parent; no concurrent or adversarial filesystem changes. No network or modification of original archive.

Run:
```sh
python -m pip install -r ../v0.2/requirements.txt
python -m unittest -v
python -O -m unittest -q
python stage_assets.py original.zip trusted-receipt.json selection.json NEW_OUTPUT_DIRECTORY
```

Receipt follows v0.1. Selection example:
```json
{"schema":1,"images":[{"source":"art/foreground.png","name":"foreground.png","format":"PNG","width":432,"height":432,"alpha":"transparent","box":[100,100,332,332],"color":null}]}
```

All selected records must pass prior archive receipt and decoded image contracts before creating output. Flat safe filenames only; unique source and case-insensitive output names; matching output format extension required. The captured archive bytes are reused for both verification and staging. Destination must be nonexistent (including dangling symlinks); exclusive file creation; ordinary write exceptions trigger cleanup of the newly created directory. Not atomic against process termination or malicious concurrent filesystem changes; inspect/remove incomplete output manually if interrupted. No existing directory replacement, automatic project import, image transformation or release approval. Manifest contains original source paths, hashes and measured image contracts; only publish after checking confidentiality, rights and provenance. Output status is staged_not_release_approved, not packaged or published. Selected bytes are held in memory within inherited archive size bounds. Actual APK asset mapping, release isolation and physical review remain separate gates.

Local Python 3.13.5 / Pillow 12.3.0: 12/12 synthetic integration tests passed in standard and optimized modes. Exact source/test blobs matched 40c57f61bc8d20c9985972022990b925f8f0a240 and 03a7a13171351c434457226ae0d0439e02e127b6. Both loaded dependency blobs matched previously committed versions. No real product archive, CI, product integration or APK verification performed. Next verify packaged assets using a real, authorized QA build and independently preserved runtime receipt; retain project-specific resource mapping and release isolation.
