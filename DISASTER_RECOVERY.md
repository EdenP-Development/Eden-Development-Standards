# Disaster recovery

## Lost or unavailable signing material
Stop distribution, preserve installed games and old APKs. Check original build receipts, owner-controlled encrypted backups, password manager and GitHub secret availability (names only). Run original certificate preflight after authorized restoration. Never expose key contents, brute force passwords or generate a substitute for an in-place update. A missing Actions secret is not proof the original key is lost.

If recovery fails, document the limitation and evaluate a separate-package migration with portable saves; owner approval required. If a key is exposed, stop signing/distribution and assess platform-specific rotation/recovery; do not assume deleting a Git commit revokes exposure.

## Lost chat or build environment
Read project handoff, latest registry, active PR/issue, source SHA and live CI. Do not assume prior sandbox files exist. Restore from durable artifacts and owner-controlled vault. Verify identity before building.

## Recovery drill
Owner privately verifies backup opens, original certificate matches registry and independent copy is recoverable. Record only status/date in public registry. Repeat before major releases and after storage changes.
