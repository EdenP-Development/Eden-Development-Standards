# EDT-09 v0.4 — Packaged asset byte verification

2026-11-25. Python 3.11+ standard library. Read-only check of byte-preserved APK assets against independently recorded runtime asset hashes and exact APK hash. No extraction, install, network, signing operations or modification.

Receipt example (replace placeholder strings with actual 64-digit hexadecimal hashes):
```json
{"schema":1,"apk_sha256":"EXPECTED_APK_HASH","required":{"assets/branding/logo.png":"EXPECTED_ASSET_HASH"},"exclusive_prefixes":["assets/branding/"]}
```

```sh
python verify_package.py candidate.apk trusted-receipt.json
python -m unittest -v
python -O -m unittest -q
```

Required hashes come from the independently approved runtime asset receipt, with explicit project-specific path mapping. The APK hash comes from the exact build receipt. Never regenerate expected asset hashes from the candidate APK merely to make verification pass. Exclusive prefixes are opt-in and reject any missing or unexpected ZIP entry under those paths, including explicit directory entries. An empty prefix list checks required files only. Other directories are not certified free of experimental content.

Rejects duplicate ZIP entries, case-colliding assets within lowercase assets/ namespace, missing manifest marker, unsafe receipt paths, missing or altered required assets, unsupported compression/encryption and nonregular required entries. Limits: 512 MiB APK, 50000 ZIP entries, 16 MiB per checked member, 1024 required members. Use a trusted stable local file and receipt, not an adversarial ZIP sandbox. Exact hash checked before and after member inspection. Manifest presence is not proof of a valid Android APK.

Scope is byte-preserved assets/ entries only. AAPT2 may transform res/ files; compiled resources, adaptive icons, qualifiers, XML overrides, signature verification and runtime resource selection require separate product-specific gates. No application launch, image rendering, rights clearance or release approval.

Actual Python 3.13.5 local runs: 10/10 tests passed in normal and optimized modes. Synthetic APK-shaped ZIP fixtures only. Exact committed blobs matched tested bytes: verify_package.py c17dca7b73df2936408ab110e3e5da03eb08db49; test_verify_package.py ccf2d61cf6a2dc82bd6436e41123101800d27453. Android SDK unavailable on PATH; no actual signed APK inspected, no CI or consumer integration verified. Next pilot with a trusted existing QA APK and independent receipt; do not change app source or build configuration merely to accommodate this utility.
