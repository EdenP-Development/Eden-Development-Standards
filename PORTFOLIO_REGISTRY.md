# PORT-02 — Living portfolio registry

Updated 2026-11-25. Management snapshot, not a release authority. APP_REGISTRY.json remains authoritative for recorded signing/distribution evidence; project branches and handoffs may contain newer facts. All commercial readiness reviews remain open unless supported by an exact acceptance receipt. Do not infer approval from a missing record.

| Product | Brand | Repository / evidence | Current documented stage | Startup adoption | Next milestone / risk |
| --- | --- | --- | --- | --- | --- |
| Sudoku | Spudacus / GridMates | [repo](https://github.com/EdenP-Development/SudokuTogether), [Beta 3 pilot](https://github.com/EdenP-Development/SudokuTogether/blob/feat/beta3-foundation/docs/BETA3_STARTUP_PILOT.md) | Beta 2 public owner-reported; Beta 3 branch active | 4.2s timing trial implemented on Beta 3 branch; CI/phone review pending | Beta 3 coach and acceptance; verify public archive/download and signer recovery |
| Word Search | Spudacus / GridMates | [PR 199](https://github.com/EdenP-Development/GridMates-Word-Search/pull/199) | Private-signed beta 124 emulator upgrade reported; physical/public acceptance unverified | 4.2s shared startup implemented in [draft PR 200](https://github.com/EdenP-Development/GridMates-Word-Search/pull/200); CI/merge/phone pending | Reconcile current branch, phone review, launch gates |
| Crossroads | Spudacus / GridMates | [PR 120](https://github.com/EdenP-Development/GridMates-Crossroads/pull/120) | Illustrated internal QA; newer active checkpoint not established | Two-stage 4.2s timing trial implemented on identity-17 branch; CI/phone review pending | Find active handoff, physical review, beta signing |
| Grid Hunt | Spudacus / GridMates | [GH-V36-H handoff](https://github.com/EdenP-Development/GridMates-Grid-Hunt/blob/feature/gh-v02-in-puzzle-map-look/docs/CURRENT_DEVELOPMENT_HANDOFF.md) | Internal alpha; GH-V36-H; QA370 baseline launch detection failed before candidate upgrade, fresh CI pending | Adopted per owner; 300/1500/300 ms in active branch; revised timing physical acceptance pending | Consolidated CI and phone QA, timing review, launcher surround and save checks |
| Sector Rebound | Spudacus | [PR 158](https://github.com/EdenP-Development/Ricochet-Rumble/pull/158) | Beta 1 preparation; stacked visual/gameflow QA, physical acceptance pending in handoff | Owner-approved standalone 2.5s integration reported merged on main | Review stacked changes, signed beta and two-device QA |
| Eden Comms | EPS | [handoff](https://github.com/EdenP-Development/Eden-Comms/blob/main/CONTINUE_HERE.md) | Visual Review 2 feedback; security prototype, not production messenger | EPS revised 3.0s source verified on main; physical acceptance pending | Visual QA, physical 54 cases and independent security review |
| The Last Taters | Spudacus (standalone) | [repo](https://github.com/PlayerEden/the-last-taters), [integration roadmap](https://github.com/PlayerEden/the-last-taters/blob/dev/0.12-visual-prototype/docs/EDENP_INTEGRATION_ROADMAP.md) | Alpha 0.12 browser staging; native PC and Android planned | Standalone startup adoption planned | Owner transfer to EdenP; verify baseline and pending recovery QA; portable saves and platform prototypes |
| Text Adventure RPG | Spudacus proposed | [repo](https://github.com/PlayerEden/text-adv-rpg) | Unknown | Unknown | Inspect source and establish status |
| Space Buddies | Spudacus proposed | Repository unverified | Unknown | Unknown | Locate project before classification |
| EPD storefronts | EPD | Not audited in GitHub inventory | Unknown | Not applicable | Storefront inventory and brand work |
| Shared infrastructure | EdenP Development | [standards](README.md) | BUS-01–07 documented, PORT-01 complete at inventory level | [Master startup guide](branding/game-startup/v1.0/README.md) | PORT-01–07 documented; operational remediation and timing acceptance pending |

## Update rules
Use dated evidence from exact source/ref, CI and owner feedback. Distinguish implemented, CI-tested, physically accepted and publicly verified. Record pending or unknown rather than guesses. Link signing evidence instead of copying credentials or mutable release fields. Product chats own product implementation; central chat owns cross-portfolio tracking and approved shared standards. Refresh only affected rows; preserve concurrent changes. Do not change pricing, publish, merge product code, transfer repos or alter signing identities merely by updating this registry.

## Current shared decision
Startup v1.0 remains historical approved baseline; v1.1 candidate is 300 ms fade-in, 1500 ms hold, 300 ms fade-out per logo. Grid Hunt source inspected; Sudoku Beta 3 and Crossroads identity-17 now implement 300/1500/300; fresh CI and physical acceptance pending. Owner feedback reopens timing review. PORT-03 additionally found owner-approved Sector Rebound 2.5s standalone timing; preserve it. Proposed split: standalone 2.5s, GridMates 4.2s; EPS independent 3.0s trial implemented. Grid Hunt and Sector Rebound adoption confirmed by owner; no mandatory timing rollout pending physical acceptance. See [branding adoption audit](PORTFOLIO_BRANDING_ADOPTION.md).

## Next
PORT-03 scoped adoption audit documented; PORT-04 scoped standards audit documented; [PORT-05 proposed priorities](PORTFOLIO_PRIORITIES.md) documented; [PORT-06 source catalog](DEVELOPMENT_TOOLKIT.md) documented; [PORT-07 review process](PORTFOLIO_REVIEW.md) documented. Continue operational remediation and product-specific milestones. Portfolio inventory scope and limitations: [PORT-01 audit](PORTFOLIO_AUDIT_2026-11-25.md).

Private portfolio records belong in access-controlled contexts, not this public registry.

Visibility correction (2026-11-25): current public document excludes identified private-project details. Earlier Git revisions may retain them; no history rewrite or repository visibility change performed.

## Toolkit checkpoint — 2026-11-25
See [current toolkit verification and recovery checkpoint](toolkit/EDT_CHECKPOINT_2026-11-25.md) for implemented versions, recorded local tests, real historical Sudoku QA artwork byte verification and remaining consumer gates. No release promotion implied.

## PORT-08 — Active portfolio reconciliation (2026-11-26)
This dated evidence supersedes older stage/next-action descriptions above where conflicting; not an exact-head release authorization. Product branches may advance independently.

| Product | Inspected evidence | Next practical gate |
| --- | --- | --- |
| Sudoku | [Active handoff](https://github.com/EdenP-Development/SudokuTogether/blob/feat/beta3-foundation/CONTINUE_HERE.md), blob 58fa0cc2915226b0cdbabbc473a895289fc62304. Prior e3fe486 quality/unsigned runs 45763304064/45763304081 independently confirmed successful; newer protocol 11 changes pending per handoff. | Name Collection and communication acceptance, linguistic/migration checks, Fire/tablet, physical LAN, rights, signed upgrade; Amazon rehearsal before later Play. |
| Word Search | [PR 199](https://github.com/EdenP-Development/GridMates-Word-Search/pull/199) reports signed build 126, shared 58dp artwork and same-certificate 125→126 emulator upgrade preserving test progress; [PR 200](https://github.com/EdenP-Development/GridMates-Word-Search/pull/200) startup draft. | Verify exact current build/branch and signing receipt; handset icon/startup review. |
| Crossroads | [Active handoff](https://github.com/EdenP-Development/GridMates-Crossroads/blob/feature/identity-17-art-import/docs/CROSSROADS_CURRENT_HANDOFF.md), blob 7208a5231e12fb2096af39ba0170fa462b203cd7. AI2-08B geometry experiment pending; AI2-08A rules passed per handoff; experimental AI not default. | Owner visual QA, balance/replay evidence, current CI, signing/upgrade readiness. |
| Grid Hunt | [Active handoff](https://github.com/EdenP-Development/GridMates-Grid-Hunt/blob/feature/gh-v02-in-puzzle-map-look/docs/CURRENT_DEVELOPMENT_HANDOFF.md), blob a8e4c6996fc503841393e5852460f604f03b610c. GH-V41-G, QA448 last all-green per handoff; coastal captures and app unit-test gate pending. | Inspect captures, verify current CI, preserve Woodland; 12-level target with migration design. |
| Sector Rebound | [Handoff](https://github.com/EdenP-Development/Ricochet-Rumble/blob/main/CONTINUE_HERE.md), blob e60cde1c96ab8d219d4d71cac7374440ead1c59b. B1-R10 head 80cd22b35b9bb285751ef82e69e1d63f3551edfe, run 45592089117 reported green; debug QA, mocked transport. | One consolidated owner review, physical two-phone, pacing, signed compatible beta and durable archive. |
| Eden Comms | [Handoff](https://github.com/EdenP-Development/Eden-Comms/blob/main/CONTINUE_HERE.md), blob ed6736d47156d71565e0e31a5722092b3b8d52fd. EC-R6, internal 10036 signed per handoff; EPS 3s splash owner accepted. | Reliability consolidation; 54 physical cases and independent security review remain mandatory. |

Shared standards now include [audio](audio/gridmates/README.md), [identity](identity/gridmates/README.md) and [communication](communication/gridmates/README.md). Sudoku is the pilot; no automatic rollout. This review inspected handoffs/PR descriptions, not all underlying workflow logs or APKs; Word Search root handoff not found, PR evidence is partial. No private-project details added. No app code, signer, store or release changes. Next PORT-09: owner-controlled signing recovery and accepted artifact preservation evidence; no secret collection.

## PORT-09 — Recovery readiness (2026-11-26)
See [owner recovery drill and channel triage](DISASTER_RECOVERY.md#port-09--owner-recovery-readiness-checkpoint-2026-11-26). Six active products reviewed against existing registry. Independent private signer recovery remains unconfirmed; no proof of loss or actual recovery. Prioritize accepted Sudoku Beta 2 archive, Word Search signed v126 and Eden Comms internal v10036, then other current QA/proof artifacts. No channel identities changed. Next PORT-10 release verification; owner recovery remains open.

## PORT-10 — Master release verification (2026-11-26)
[Master procedure and technical receipt](RELEASE_CHECKLIST.md#port-10--master-release-verification-procedure-2026-11-26) extend existing release/save/recovery policy. EDT-02 real SDK/emulator execution remains unverified; no dispatch, signing or product changes. Proposed Sudoku signed Beta 3 receipt pilot after actual candidate/baseline availability; next PORT-11 verified GridMates handoffs. No publication authorization.

## PORT-11 — GridMates adoption (in progress, 2026-11-26)
Communication pilot evidence reconciled in communication/gridmates/README.md. [Progression and collections conventions](PORTFOLIO_STANDARDS_ADOPTION.md#port-1102--gridmates-progression-and-collection-conventions-proposed-2026-11-26) proposed from four inspected product records; no universal ledger or automatic rollout. Sudoku pilot acceptance remains prerequisite. Next bounded adoption checklist and implementation handoff gate; no product or publication changes.

## PORT-12 — Commercial readiness (in progress, 2026-11-26)
Storefront lanes documented in COMMERCIAL_READINESS.md (12.01), privacy hosting proposal and rights triage in PRIVACY_STANDARDS.md (12.02), lightweight support operations in CUSTOMER_SUPPORT.md (12.03). No live service or rights clearance established. Next PORT-12.04 public site and storefront asset framework; owner approval required for deployment/contact, Sudoku pilot acceptance remains open. PORT-11.03 consumer adoption framework documented in PORTFOLIO_STANDARDS_ADOPTION.md; no automatic rollout.

## PORT-12.04 — Website prototype (2026-11-26)
[Undeployed static prototype and receipt](website/prototype/README.md) committed; exact source readback and ten limited static checks passed. No browser/device rendering, live link testing, host selection, deployment, policy/contact publication or product changes. PORT-12.05 remains dependent on Sudoku rehearsal; PORT-13 can proceed independently. PORT-11.03 adoption framework complete at documentation level; pilot acceptance remains open. No application registry channel changes.

## WEB-03B / WEB-04 preparation (2026-11-26)
Website prototype README now records prior four-viewport Chromium evidence, 48px profile-link correction and pending browser retest. Pinned branding guides inspected; binary retrieval failed, no artwork integrated. No deployment or app changes. PORT-13 may proceed independently.

## WEB-04 — Canonical branding integrated (2026-11-26)
Binary retrieval resolved with base64; three pinned Git blobs match main. Website preview now references existing local Spudacus, GridMates and EPS PNGs, commit 8500a13ed1945cca81175d9393e29e270a0776c7. See website/prototype/README.md for exact evidence and limitations. Browser retest, decoded SHA-256 and owner visual approval pending. No deployment or product changes.

## WEB-04C — Branded browser reflow (2026-11-26)
All three local artwork SHA-256 checks passed. Corrected HTML b23b08ea6b1133a4d97d54d9ed0807cd2282628c passed no-overflow checks at four ordinary viewports and two enlarged-root-text cases. Ordinary navigation passed; enlarged navigation geometry assertion requires diagnosis. See website/prototype/README.md for scoped evidence. No deployment or product changes.

## WEB-05.01 — Sudoku product page pilot (2026-11-26)
WEB-04D navigation discrepancy resolved in previous browser checkpoint (24/24 checks, computed scroll margin); see website/prototype/README.md. New Sudoku page and homepage link committed and exact-readback verified, 16 href references statically checked. No new browser acceptance, live storefront verification, publication or app changes. Next consolidate CSS and test both pages before expanding. PORT-12.05 and owner policy/contact decisions remain open.

## WEB-05.02 — Shared stylesheet (2026-11-26)
Both prototype pages now use site.css; exact readbacks and 18 static href checks passed. Existing body content preserved, product heading rule scoped. Browser regression of external stylesheet and product navigation pending; see website/prototype/README.md. No deployment or product changes.

## WEB-05.03 — Browser regression harness (2026-11-26)
Reusable browser_smoke.py committed and exact readback verified; full execution remains blocked in current container by administrator navigation restriction (minimal intercepted-origin probe failed). No multi-page browser pass claimed. See website/prototype/README.md for commands and scope. Next permitted execution and remaining product pages. No deployment or app changes.

## WEB-05.03B — Website quality workflow (2026-11-26)
Read-only website-preview.yml committed and exact-readback verified, commit e3b6c0a6afef44d4504dab2c15e6fc73e358681c. Actual workflow execution not established; browser acceptance remains pending. Next draft remaining product pages with shared CSS, extend browser coverage, verify actual run. No deployment.

## WEB-05.04 — Full website product portfolio (2026-11-26)
All six active public-facing product concepts have preview pages linked from homepage; five new source-backed development pages and expanded browser harness committed and exact-readback verified. Static 63 href checks passed, seven HTML pages. Actual expanded browser execution, product-specific artwork, copy acceptance, approved support/privacy information and hosting remain pending. See website/prototype/README.md. No app or storefront changes.

## WEB-05.05B — Artwork recovery and intake (2026-11-26)
Website asset manifest committed and readback verified. Four QA archive metadata records checked; urgent Eden Comms historical visual archive recovered, local digest matched and unshared Drive copy uploaded (metadata verified, remote rehash pending). Remaining archives and individual product artwork pending. No website asset approval or deployment. See website/prototype/README.md.

## WEB-05.05C — Candidate archive preservation (2026-11-26)
Four candidate archives now locally checksum verified and uploaded to unshared Drive; metadata sizes verified, remote rehash pending. 248 image files decoded and inventoried; representative private contact sheets prepared. Manifest and website handoff updated. No approved product imagery integrated, no deployment or app changes.

## WEB-05.05F — Website artwork candidate exports (2026-11-26)
Sudoku original branding and three Crossroads QA archives locally hash verified and privately preserved with metadata readback. Three optimized Sudoku website derivatives prepared, candidate manifest updated; no publication approval. Crossroads icon blob confirmed but byte retrieval empty. No website binary integration or deployment.

## WEB-06.01 — Sudoku privacy/support candidates (2026-11-27)
Two explicitly unpublished Markdown candidates committed under website/drafts, exact readbacks verified. Beta 3 privacy source scoped separately from public Beta 2; installation/save-safe support draft. Publisher/contact, release verification, current policy/audience review, support drills, stable approved URLs and deployment open. No live policy or support service established.

## WEB-06.02 — Publication receipt preflight (2026-11-27)
Reusable offline receipt template, validator, synthetic tests and usage guide committed. Exact source blobs matched locally; 11/11 tests passed. Structural validation only; no real product approval, hosting or deployment. Next harden fixture separation and prepare explicit allowlisted packaging gate.

## WEB-06.03 — Publication quality gate hardening (2026-11-27)
Publication validator v0.2 production/fixture separation and exact content metadata checks committed; exact local Git blobs matched, 16/16 tests passed. New read-only publication CI workflow committed, execution unverified. Documentation synchronized. No real publication approval or deployment. Next allowlisted packaging with leakage regressions; artwork and browser acceptance still open.

## WEB-06.04B — Review packaging verification (2026-11-27)
Pinned review-only packager with explicit eleven-file allowlist and integrity receipt; eight new tests and sixteen prior tests actually passed (24/24). Three canonical local art hashes matched. CI review ZIP build/retention configured, exact source readback verified; actual full ZIP and CI execution pending. No publication or deployment; website and toolkit handoffs synchronized.

## WEB-06.04C — Complete offline review ZIP (2026-11-27)
Eleven pinned source fingerprints matched, actual 24/24 regression rerun passed. Complete review ZIP built and independently verified (12 entries, 852575 bytes, SHA256 e9b3b780e5cb772150be6104b499c775793ab52969e65bb73e4af60f844d5503); delivered in chat, publication_authorized=false. Full browser/CI acceptance and hosting decision remain open. No deployment or app changes.

## WEB-07.01 — Consolidated isolated website verification (2026-11-27)
Exact review ZIP rechecked; 70 local references resolved and 42/42 actual isolated Chromium layout configurations passed. Direct file navigation blocked, so full navigation suite and CI remain unverified. Acceptance note and handoff synchronized. No deployment or app changes. Next hosting evaluation and remaining release gates.

## WEB-08.01 — Brand separation redesign (2026-11-27)
Five new candidate pages and separate stylesheet committed under website/redesign, original prototype and packaging pins preserved. Static local reference checks: 57, errors 0. See website/redesign/README.md. Transitional links to original product pages; browser/visual acceptance, redesigned return navigation and artwork approval pending. No deployment or app changes.

## WEB-08.02 — Direct brand voice (2026-11-27)
Five redesign pages simplified and existing brand standard updated to reflect practical, personal, context-dependent communication without forced slogans or corporate language. Exact readbacks and unchanged resource/navigation references verified. See website/redesign/README.md. Original baseline preserved; visual review and redesigned product navigation pending. No app changes or deployment.

## WEB-08.03 / WEB-08.04A — Redesigned product routes and visual hierarchy (2026-11-27)
Six product routes integrated in c5c2d81337d7ae9c988951bf14c892ff231f9359; 111 local references across 11 pages passed static checks. Product accent treatments and listing hierarchy implemented; see [redesign handoff](website/redesign/README.md). Candidate artwork still awaits individual clearance and byte verification. Browser acceptance, owner visual review, packaging and deployment pending. Original prototype and apps unchanged.

## WEB-08.04B — Sudoku artwork recovery (2026-11-27)
Original branding archive retrieved and exact recorded SHA-256 matched. Six individual image checks passed (hash, dimensions, mode); visual contact sheet inspected. Proposed hero/wordmark/card selection documented in [redesign handoff](website/redesign/README.md). Website approval and integration pending; no publication or app changes.

## WEB-08.04C — Offline Sudoku artwork pilot (2026-11-27)
Two-page private review ZIP built and integrity checked; eight isolated Chromium layout checks passed. Direct file navigation blocked; full redesign integration and owner approval pending. See [website handoff](website/redesign/README.md). No public binaries or deployment.

## WEB-08.04D — Word Search artwork recovery (2026-11-27)
Verified historical screenshot archive, selected three images for private expanded GridMates pilot, 10 payloads checked after ZIP readback. Browser acceptance and public artwork clearance pending. See [redesign handoff](website/redesign/README.md). No deployment or app changes.

## WEB-08.04E — Grid Hunt artwork pilot (2026-11-27)
Recovered and verified 50 coastal sprite exports; six used in four-page private GridMates pilot. 17 payload hashes and 43 local references passed. Browser and publication approval pending. See [redesign handoff](website/redesign/README.md). No app or deployment changes.

## TAT-PORT-01 — The Last Taters revival (2026-11-27)
Owner direction: browser-first itch.io development, eventual downloadable PC and Google Play. Project integration roadmap and handoff committed; current personal repository remains canonical until owner transfer to EdenP-Development is verified. Preserve history, existing browser saves and standalone Spudacus identity. Shared standards mapping is documented; native readiness, signing, release and asset/data acceptance remain open. No publication or ownership change performed.

## WEB-08.04F — Crossroads artwork pilot (2026-11-27)
Verified historical QA archive and APK; recovered four original environment images and expanded private GridMates pilot to five pages. 22 payload hashes and 57 local references passed. Browser acceptance, gameplay screenshots and public artwork clearance pending. See [redesign handoff](website/redesign/README.md). No app or deployment changes.
