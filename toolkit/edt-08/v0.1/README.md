# EDT-08 v0.1 — Baseline integrity verifier

2026-11-25. Original Python 3.11+ standard-library utility inspired by the Town baseline integrity pattern. Read-only; no network, runtime execution or modification of files. Given a trusted, independently preserved JSON manifest, verifies listed relative paths and SHA256 hashes under a stable local directory.

Manifest schema:
```json
{"schema":1,"files":[{"path":"assets/example.png","sha256":"REPLACE_WITH_ACTUAL_64_HEX_DIGEST"}]}
```
The example contains a placeholder, not a valid digest. Record the actual accepted bytes and preserve the manifest separately from the candidate; never regenerate expected hashes just to pass a failing gate.

```sh
python verify_baseline.py --root /path/to/project --manifest /path/to/trusted-manifest.json
python -m unittest -v
python -O -m unittest -q
```

Returns JSON on success; nonzero exit on verification failure. Rejects empty manifests, unknown schema/fields, duplicate paths or JSON keys, traversal, absolute paths, backslashes, colon, missing files, symlinks in listed relative paths and invalid/mismatched hashes. Only use on a trusted, stable checkout or archive directory: no adversarial concurrent filesystem changes, no claim of race-proof sandboxing. Does not detect unlisted files, validate manifest authenticity, establish legal rights, parse JavaScript, validate APK signing, or test runtime behavior. Root itself is resolved; listed paths are checked relative to it. Do not use private filenames or sensitive hashes in a public manifest.

Actual local standard and optimized Python executions each passed all 12 unit tests. Exact Git blobs matched tested source d36a65add512ea477bd9bf40c8521c7d8d2f9037 and tests b47b9eee416e5e2a7232d225276f57d47126e463. No consuming-project integration or actual release archive validation yet. Next pilot against an independently preserved known baseline, without replacing project-specific static or runtime gates.
