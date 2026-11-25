# EDT-02 v0.1 — Read-only APK upgrade preflight

Initial isolated-tested candidate, 2026-11-25. New Python implementation inspired by the Grid Hunt upgrade-verification pattern; no game source copied, no third-party Python dependencies or license changes. Python 3.11+ and locally trusted Android SDK build-tools aapt/apksigner required for real APKs.

Run:
```sh
python preflight.py old.apk new.apk --package EXPECTED_PACKAGE --signer EXPECTED_SHA256 --aapt /path/to/aapt --apksigner /path/to/apksigner
python -m unittest -v
```

Obtain expected package and certificate fingerprint from trusted accepted release receipts / APP_REGISTRY.json, never solely from the candidate. Supply exact preserved APKs and trusted tool paths. The script reads APK hashes, package, versionCode and signature verification output; rejects unexpected package/cert, multiple signers, non-increasing versions and identical bytes. Emits JSON on pass and nonzero exit on failure. It does not compare to expected archived APK hashes: compare the reported hashes with independently recorded receipts. Supports single-signer standalone APKs and ordinary version codes only, not signer rotation, split APKs, AABs or versionCodeMajor. No device operations, keys, passwords, network or save access.

Local Python tests: 6 passed, including six rejection subcases; mocked SDK command outputs and synthetic files. Local tested source SHA256 5087b859b5d92966787871960f2408823959010456366a23d18815a0403cb124 and tests SHA256 89c7e072eab9c9a222ca40647b9bd24a80aea06d890f55a91b7aa96c08fd4f66. Android SDK tools unavailable in local test environment. No actual APK verification, CI or consuming-project acceptance claimed. Next run against known compatible and incompatible disposable QA APK pairs using actual SDK tools; then add an isolated emulator install-over harness with explicit device serial, synthetic fixture and no uninstall/clear. Static pass never replaces actual install-over, data preservation, key custody or release approval.

See SAVE_PRESERVATION.md, RELEASE_CHECKLIST.md and DEVELOPMENT_TOOLKIT.md at repository root.
