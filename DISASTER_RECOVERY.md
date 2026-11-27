# Disaster recovery

## Lost or unavailable signing material
Stop distribution, preserve installed games and old APKs. Check original build receipts, owner-controlled encrypted backups, password manager and GitHub secret availability (names only). Run original certificate preflight after authorized restoration. Never expose key contents, brute force passwords or generate a substitute for an in-place update. A missing Actions secret is not proof the original key is lost.

If recovery fails, document the limitation and evaluate a separate-package migration with portable saves; owner approval required. If a key is exposed, stop signing/distribution and assess platform-specific rotation/recovery; do not assume deleting a Git commit revokes exposure.

## Lost chat or build environment
Read project handoff, latest registry, active PR/issue, source SHA and live CI. Do not assume prior sandbox files exist. Restore from durable artifacts and owner-controlled vault. Verify identity before building.

## Recovery drill
Owner privately verifies backup opens, original certificate matches registry and independent copy is recoverable. Record only status/date in public registry. Repeat before major releases and after storage changes.

## PORT-09 — Owner recovery readiness checkpoint (2026-11-26)
Use existing SIGNING_KEY_MANAGEMENT.md, APP_REGISTRY.json and RELEASE_CHECKLIST.md; this is a practical extension, not a new signing policy. Registry inspected at blob aaeb7d40e3b7b9e4dacd9997bf5961f8d8dced4d. Six active products reviewed; no independently recoverable private signer backup confirmed from the inspected records. Unconfirmed is not lost.

| Priority / channel | Current evidence | Required owner action |
| --- | --- | --- |
| P0 Sudoku public Beta 2 successor v31 | Organization signing verified; public release owner-reported; registry APK hash missing | Verify two independent encrypted copies, original certificate and exact accepted APK archive; independently verify public download |
| P0 Word Search beta v126 | Signed APK and pinned certificate recorded; owner playtest scope | Recover both private copies and preserve exact signed candidate and receipt; do not mark public |
| P0 Eden Comms internal v10036 | Private signer and APK recorded; internal only | Recover both copies and exact signed archive privately; security gates unchanged |
| P1 Grid Hunt beta | Signed proof v10302, unpublished | Verify backup recovery before distributing; preserve proof separately from QA |
| P1 Sector Rebound | Private beta signing proof reported; channel reconciliation needed; historical production encrypted backup exposure recorded | Reconcile actual beta certificate/package privately; assess historical exposure separately, no automatic rotation or use of historical blob |
| P1 Crossroads | Production signer unverified; QA public test only | Locate existing intended channel and evidence before provisioning any new key |
| Historical Sudoku Beta 1 | Original signer unresolved | Preserve existing installs/APK and migration evidence; no replacement key for same package |

Public/ephemeral QA keys are not confidential production identities. Do not promote them. No channel records changed in this checkpoint.

### Owner-controlled recovery drill
1. In a trusted local environment, locate existing primary encrypted keystore and independent recovery copy. Use existing vault and password manager, not a new duplicate cloud archive. Ensure access recovery does not depend on the same single device/account.
2. Restore each copy separately to a temporary private directory; verify readable original key entry and certificate SHA-256 against exact channel registry. A matching public certificate alone does not prove possession of the private key: confirm private-key operation using a harmless local signing fixture or approved isolated preflight. Never publish the fixture.
3. Verify the exact accepted APK or candidate with apksigner/aapt and SHA-256, match package, certificate and version to receipt; archive original bytes, source commit, build instructions, dependency/SDK versions and test evidence. Do not substitute a rebuild for the accepted bytes. Distinguish ZIP hash from APK hash.
4. Reopen the independent archive, verify byte hashes and recovery instructions; keep private rights receipts, master assets and player data separate from public metadata. Actions artifacts expire and secrets cannot be retrieved as backups. Prioritize expiring accepted/review artifacts; no automatic release download or upload.
5. Record only channel, date, primary/secondary recovery result, certificate match, private-key operation result, archive byte check, source ref, remaining blockers and owner confirmation in the public registry as appropriate. Private paths, aliases, passwords, recovery codes, key bytes and account details stay private. Clean temporary copies securely according to local storage policy; no secrets in command arguments or logs.
6. Repeat before major releases and after storage/account changes. If missing/mismatched, stop affected distribution; preserve installed data, investigate original recovery, require owner decision for migration. No uninstall workaround.

### Artifact triage
First preserve Sudoku public Beta 2 exact bytes (registry hash missing), Word Search v126 signed owner candidate and Eden Comms v10036 signed internal candidate, then current Grid Hunt and Sector Rebound consolidated QA and other accepted baselines. Check existing owner-controlled archives before retrieving artifacts; never duplicate unnecessarily. Record artifact expiry from actual service metadata if available, not guessed. Keep debug/QA/public channels distinctly labeled. No production publication or storage transfer authorized by this checkpoint.

Next PORT-10: unify release evidence and upgrade verification using existing release checklist and EDT-02, with actual SDK/emulator execution and a bounded consumer pilot where available. This checkpoint is documentary only: no backup recovery, APK download, signing, key transfer, new secrets, game changes or physical tests performed.

## Eden Comms recovery reconciliation — 2026-11-27
For current triage supersede historical internal v10036 with frozen internal 10049 and same-signer predecessor 10048. See [EC-B07 exact archive inventory](https://github.com/EdenP-Development/Eden-Comms/blob/main/docs/DURABLE_RECOVERY_ARCHIVE.md) and [EC-B08 physical matrix](https://github.com/EdenP-Development/Eden-Comms/blob/main/docs/TWO_PHONE_ACCEPTANCE_MATRIX.md). Visual evidence expires Nov 28, Preview Nov 29, private APKs Dec 3 (UTC; exact timestamps in inventory). Metadata only verified; durable copies, byte verification, independent signer recovery and physical 0/54 remain open. No other product triage or signing identity changed.
