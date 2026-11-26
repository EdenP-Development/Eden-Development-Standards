# Release checklist

- [ ] Identify channel, previous accepted APK, package, signer and version.
- [ ] Verify private custody and independent recovery copy.
- [ ] Pin exact reviewed source commit and run original signer preflight.
- [ ] Run relevant unit, UI, lint and gameplay tests; document deferred checks.
- [ ] Verify release APK package, signer, increasing version, hash and permissions.
- [ ] Verify actual install-over and save preservation using backed-up noncritical data.
- [ ] Verify export/restore when supported.
- [ ] Review product, series and creator attribution against BRAND_IDENTITY.md; record visual approval or deferral.
- [ ] Review player-facing copy, screenshots, privacy and applicable disclosures.
- [ ] Obtain explicit owner approval for publication.
- [ ] Archive exact APK and receipt; verify downloadable bytes.
- [ ] Update registry and project handoff with evidence and outstanding risks.

## PORT-10 — Master release verification procedure (2026-11-26)
Apply the existing checklist above, RELEASE_POLICY.md, SAVE_PRESERVATION.md and DISASTER_RECOVERY.md. This is an evidence workflow, not automatic release authorization or a replacement for project CI. Use the existing commercial/Play receipts when applicable.

| Stage | Required evidence | Stop condition |
| --- | --- | --- |
| Scope | Named product/channel, exact candidate source, previous accepted artifact, advertised scope and intended platform | Unknown baseline for an update or ambiguous identity |
| Automated QA | Exact-head build, unit tests, lint, relevant runtime/UI/asset checks; record executed vs compiled tests | Required checks fail or are missing |
| Signing | Owner recovery status, trusted original signer preflight, exact signed artifact hash, package/certificate/version, permissions | Wrong identity, unverified required custody, missing hash or non-increasing update version |
| Upgrade | Actual prior distributed APK to exact candidate on controlled device with backed-up synthetic/noncritical progress; cold launch, save/profile/reward/settings and supported export/restore checks | Data loss, incompatible signature, destructive workaround or missing mandatory evidence |
| Physical | Named build/device/OS, actual core workflows, accessibility, offline and two-device tests where relevant | Critical defects or unaccepted mandatory checks |
| Readiness | Exact inventory rights and privacy, platform/audience declarations, support route, honest listing, applicable security gates | Unresolved mandatory rights/security/privacy/release blocker |
| Authorization | Explicit owner decision for exact artifact and channel | No approval |
| Archive/publication | Preserve exact bytes and receipt; approved distribution only; verify downloaded bytes and update handoff/registry | Missing durable archive or unexpected distributed bytes |

For first releases, explicitly record no previous distributed baseline; test clean install and appropriate same-channel upgrade rehearsal, not a fictional prior release. A QA or unsigned candidate is never promoted merely by passing tests. Record each gate as passed, failed, pending, not applicable (reason), or owner-accepted low-risk deferral (scope/reason/date). Critical security, data-loss, identity and rights requirements are not waived by a numeric score or unrelated test pass. New candidate bytes/source invalidate affected evidence; keep prior receipts.

### Technical release receipt (fill once per candidate; link from project handoff)
- Product, channel, candidate source SHA, build workflow/run/job, build scope (debug/unsigned/signed), versionCode/name, package, certificate SHA-256 and exact APK SHA-256.
- Previous accepted source/package/certificate/version/APK hash and archive reference (or first-release rationale); ZIP and APK hashes distinct.
- Owner recovery evidence date/status only; no keys, paths, passwords or secret values.
- Automated check results and links; distinguish compile, mocked/JVM, executed emulator, physical owner feedback and independent review.
- Upgrade: exact old/new hashes, device/OS, fixture categories, pre/post observations, cold-launch and export/restore results, failures and limits. No uninstall/clear workaround.
- Rights/data/storefront/security receipts, known defects, permitted deferrals, owner acceptance for exact artifact, durable archive verification, publication/download receipt and next handoff. Keep private material in access-controlled records. Commercial and Play receipts extend this record rather than duplicate it.

### Existing tooling and bounded adoption
EDT-02 v0.2 (toolkit/edt-02/v0.2/README.md) verifies two independently recorded APK hashes, expected package, single signer and increasing ordinary versionCode using trusted aapt/apksigner. Scope: ordinary monolithic APKs; split/major-version detection incomplete. No device or save access in preflight. Synthetic emulator fixture is hardcoded com.example.edtfixture; never pass product APKs to it or run it on a personal device. Fifteen mocked tests previously recorded; real SDK/emulator workflow .github/workflows/edt-02-preflight.yml remains unverified. Current connector commit-run lookup returned no PR-triggered runs; does not establish failure or success. No workflow dispatch available through inspected connector actions. Next obtain actual run ID from Actions (manual dispatch if owner chooses) and verify both jobs before toolkit acceptance. Product-specific CI remains authoritative for real save schemas; use Word Search signed 125→126 evidence as documentary reference, not as an EDT-02 execution. Sudoku Beta 3 proposed first practical release receipt pilot when exact signed candidate and accepted baseline bytes exist; no signing or release authorized here.
