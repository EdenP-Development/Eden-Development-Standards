# EDT-02 v0.2 — Receipt-bound preflight

2026-11-25. New candidate; v0.1 preserved. Python 3.11+ and trusted Android SDK tools. Requires independently recorded package, single signer SHA256, both exact APK SHA256 values and both ordinary version codes. ZIP manifest presence and reported split/major-version indicators checked; unsupported APK variants are out of scope (badging alone is not proof that all split/major variants are detected). No install or save access.

```sh
python preflight.py old.apk new.apk --package EXPECTED_PACKAGE --signer CERT_SHA256 --old-hash OLD_SHA256 --new-hash NEW_SHA256 --old-version 1 --new-version 2 --aapt /trusted/aapt --apksigner /trusted/apksigner
python -m unittest -v
python sdk_smoke.py
```

Ten unit-test methods authored, not executed in this checkpoint. SDK smoke constructs temporary manifest-only APKs with an ephemeral fixture key, checks certificate independently using keytool export, accepts compatible versions and rejects wrong package/downgrade. No real player APK, production key, phone or save involved. Scoped GitHub Actions workflow added; execution and results unverified. Local environment has no aapt, apksigner or adb on PATH. No consumer acceptance. Next verify exact CI, improve manifest variant detection with actual SDK evidence, then implement separately gated disposable-emulator upgrade test. Static verification never proves install-over or save preservation.
