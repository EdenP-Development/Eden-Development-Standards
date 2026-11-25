# EDT-09 v0.1 — Verified asset archive intake

2026-11-25. Original Python 3.11+ standard-library verifier, inspired by ARTWORK_PIPELINE.md. Given independently preserved pre-transfer archive and member hashes, verifies the exact ZIP bytes and complete expected file inventory. No extraction, file changes, network or image transformations.

Receipt schema (replace placeholders with actual independently recorded 64-digit hexadecimal hashes):
```json
{"schema":1,"archive_sha256":"ARCHIVE_SHA256","files":[{"path":"art/example.png","sha256":"MEMBER_SHA256"}]}
```

```sh
python verify_assets.py original.zip trusted-receipt.json
python -m unittest -q
python -O -m unittest -q
```

Rejects unexpected/missing/duplicate entries, case-colliding file paths, file/directory prefix conflicts, unsafe path segments and reserved Windows names, symlinks/nonregular entries, encrypted entries and unsupported compression. Only stored/deflated regular files; explicit directory entries and Unicode/space filenames are outside this conservative v0.1 contract. Limits: 64 MiB archive, 16 MiB member, 128 MiB declared total, 1024 members. Reads bounded archive bytes into memory before hashing and parsing, then reads members individually. Use local trusted receipts, not hashes regenerated from the received archive. The tool is not a hostile-archive sandbox and does not authorize extraction; directory-case consistency and additional malformed/unsupported ZIP variants need further review before extraction support.

Local normal and optimized Python runs each passed 14 tests using synthetic fixtures. Exact committed source blob 6cb9ac7a8f38f1700cac91c3d3729f7df917d994 and test blob 6166b38f7d48391a71ef3e6550b663e58a21a069 matched local tested bytes. Real artwork archive consumer integration not yet verified. Image formats, dimensions, alpha, transparent gutters, visual quality, rights, provenance, approved runtime selection and packaged APK verification are separate gates; no actual image decoding in v0.1. Next: image-specific validation of actual encoding and dimensions using bounded decoding, then controlled staging of explicitly selected verified assets. Preserve original artwork and existing project gates.
