# Eden Development Toolkit — verification checkpoint, 2026-11-25

Shared candidates, not released SDK or universal product acceptance.

| Component | Current candidate | Recorded local regression | Remaining gate |
| --- | --- | --- | --- |
| EDT-01 | v0.2 | 26 JVM cases reported passed | Android adapter and consumer |
| EDT-02 | v0.2 | 15 Python cases reported passed | actual SDK and emulator CI logs |
| EDT-03 | shared startup reference | product-specific evidence | exact-head CI and physical acceptance |
| EDT-04 | inspected theme pattern | no shared extraction | consumer need |
| EDT-05 | v0.1 generator + v0.2 analysis | 26 Node tests passed | consumer prototype and geometry verification |
| EDT-06 | inspected bot pattern | no shared extraction | consumer need |
| EDT-07 | generic simulation reuse candidate | no shared extraction | private review and rights |
| EDT-08 | v0.1 | 12 Python cases reported passed | consumer baseline |
| EDT-09 | v0.1–v0.5 | 56 local cases across five versions; v0.5 real historical Sudoku two-drawable pilot passed | current-head consumer integration and runtime resource verification |

Prior local evidence is recorded in version READMEs; this checkpoint did not re-run those suites. The cumulative 109 cases (101 previously reported, 8 newly executed) are not a measure of release readiness. Only the v0.5 suite was newly executed here.

## Real QA artifact inspection
Sudoku Visual 4 historical QA run 45550962814, artifact 14993249624, source 96747991e98f78c90e10d6eda447d1be085a3674. Retrieved actual ZIP, 42830639 bytes, SHA256 1a1d26951560641f30d3caa6bef24b633d2c27492eb1235a55815632bc100b07 matches GitHub artifact metadata. APK SHA256 fa8cf012c1a0fa458da5cc8301e50aa34046a9c964f8bfa51e792ba8906a292a matches bundled SHA256SUMS. Bundled badging reports isolated package com.playereden.sudokutogether.qa.beta3visual4 versionCode 31. Not a public beta or current-head build. Actual ZIP member bytes independently hashed:
- res/drawable-nodpi-v4/spudacus_v1_full_transparent.png: 74773dbda822161f73a639f959e8bce5c6e0b333a94ebeb8ee27f620d4995d25
- res/drawable-nodpi-v4/gridmates_v1_runtime_transparent.png: eef6d631cac0b9523f7e0dbebac229f9a2458d36fe2e73e111d251704d9ff292

Matches pinned master hashes. Manual independent ZIP inspection, not EDT-09 v0.4 execution: that tool deliberately supports assets/ only. No independent signature verification, emulator/phone test, actual runtime resource selection or launcher verification. Artifact metadata expiry 2026-12-09T05:10:38Z; durable owner archive not established. Next pilot: explicit resource mapping for byte-identical entries, separately validate transformed Android resources; do not expand v0.4 silently. Check exact EDT-02 workflow logs before consumer rollout.

## Public documentation boundary
Repository visibility verified via authenticated metadata. Current public audit, registry, priorities and toolkit catalog sanitized to remove identified private project specifics; prior revisions may remain accessible. No history rewrite, visibility change or private source publication authorized. Review remaining public history and any further exposure privately; owner decision required for history remediation.

No product source, APP_REGISTRY signing records, release or storefront changed. Next resume from this checkpoint and current product handoffs, not stale artifact links.

## EDT-09 v0.5 — executed drawable pilot
[Version 0.5](edt-09/v0.5/README.md) adds explicit byte-preserved PNG drawable mapping, separate from v0.4. Actual local Python normal and optimized runs passed 8/8 tests; exact committed blobs matched. Executed on real historical Sudoku Visual 4 APK from artifact 14993249624: both master logo hashes matched; status mapped_drawable_bytes_match. No Android resource resolution, signature, current-head, CI adoption or runtime verification. No product changes. Next prioritize targeted consumer adoption and EDT-05 only when a consumer need is established.

## EDT-05 v0.1 — deterministic maze graph
[Version 0.1](edt-05/v0.1/README.md) original standalone ES module with versioned seed contract, bounded dimensions, connected tree, straight preference and optional extra edges. Actual Node 22.16.0 14/14 tests passed; exact committed blobs match. Golden fixture established from observed initial implementation after correcting guessed expectation. No browser, Android, consumer or multiplayer verification; no existing generation behavior modified. Cumulative recorded local cases now 123, of which 14 executed in this checkpoint. Test counts do not establish readiness.

## EDT-05 v0.2 — graph analysis checkpoint
[Analysis and pathfinding](edt-05/v0.2/README.md): exact v0.1 generator 14/14 rerun; v0.2 12/12 passed in Node 22.16.0. Committed blobs match local tested bytes. Cumulative current toolkit test count 135 (109 previously recorded plus 26 EDT-05 cases; no double counting reruns). No product changes or consumer acceptance. Frozen maze-v1 seed contract retained.

## Verified EDT-05 v0.1 checkpoint
Node.js 22.16.0: 14/14 tests passed; exact source and test blobs 0d79ae47c1d3db7ce706d11edb1acbb454d9c831 and 1a7561e4fe4603f8c141c5193ab35729b48b05ba matched. 300 seeded configurations plus maximum grid and golden fixture. No consumer integration. Preserve maze-v1 algorithm and all configuration fields; new behavior requires new version. This is a v0.1 regression rerun, not additional coverage. Latest recorded cumulative count remains 135 including v0.2; v0.2 was not rerun in this checkpoint.

## EDT-06 v0.1 — Arcade objective selection
[Original decision engine](edt-06/v0.1/README.md) implemented and locally executed: Node 22.16.0 14/14 tests passed, including 108 scenarios; exact committed blobs match. Deterministic eligibility/scoring, critical health override and trace. Provisional weights; active actor lifecycle, perception, movement and balancing external. No consumer integration. Cumulative recorded toolkit cases 149 (135 previously recorded plus 14 newly executed). Next objective persistence and perception adapter; no product changes.

## EDT-06 v0.2 — Objective persistence and perception memory
[Controller](edt-06/v0.2/README.md) implemented and tested. Actual Node 22.16.0 combined suite 28/28 passed (14 prior rerun plus 14 new); exact committed source/test blobs match. Score-margin hysteresis, emergency override, eligibility recheck, tick-bounded last observed position independent of engagement permission. No consumer integration, target identity tracking or actual perception/balance verification. Cumulative recorded toolkit cases 163 (149 prior plus 14 new). No product changes.

## EDT-07 v0.1 — Autonomous simulation utility selection
[Original generic selector](edt-07/v0.1/README.md) implemented: actual Node.js 22.16.0 local tests 15/15 passed, including 192 scenario combinations; exact committed source/test blobs match. Normalized needs and personality, explicit task availability, survival priority and score trace. No private source copied, no learning, reservations, time progression or actual world execution. Emergency priorities override risk penalties, so callers must exclude unsafe tasks. No consumer integration or product changes. Cumulative recorded toolkit cases 178 (163 previously recorded plus 15 new); prior suites not rerun here. Next deterministic task reservations and conflict resolution.

## EDT-07 v0.2 — Task reservations
[Reservation module](edt-07/v0.2/README.md) implemented; actual Node 22.16.0 18/18 tests passed, exact committed blobs matched. 500 requests for 50 tasks produced 50 unique owners and order-independent results. Single authoritative caller, one active claim per agent, tick expiry, owner release, renewal and deterministic priority. No fairness, distributed synchronization, world execution or consumer acceptance. Cumulative recorded cases 196 (178 prior plus 18 new); earlier suites not rerun. Next separate experience/learning module. No product changes.
