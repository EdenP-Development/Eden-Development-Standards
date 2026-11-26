# PORT-06 — Eden Development Toolkit: source catalog v0.1

2026-11-25. Catalog of inspected implementations and reuse candidates, not a released shared library. Each adopter must review rights, dependencies, exact source, tests and integration. No code copied from private or third-party projects into this public catalog. Blob IDs identify inspected bytes; branch links may advance.

| Candidate | Source / inspected blob | What exists | Reuse boundary |
| --- | --- | --- | --- |
| EDT-01 Safe preference reads | [Grid Hunt SafeSaveReads.kt](https://github.com/EdenP-Development/GridMates-Grid-Hunt/blob/feature/gh-v02-in-puzzle-map-look/app/src/main/java/com/playereden/gridmates/gridhunt/SafeSaveReads.kt), 73f1aeddec43ea07263a2aaa2c25e0fc640c14a8 | Typed int/bool/string/set reads with ClassCastException fallback and defensive set copying; [instrumentation tests](https://github.com/EdenP-Development/GridMates-Grid-Hunt/blob/feature/gh-v02-in-puzzle-map-look/app/src/androidTest/java/com/playereden/gridmates/gridhunt/SafeSaveReadsTest.kt) blob c410ebd510c72b90c7973afa84857a8c423bac03 cover missing/wrong/valid data and unrelated keys | Adapt for non-sensitive settings; fallback is not semantic validation, recovery, migration or authorization. Never use permissive defaults for security decisions. Tests inspected, not run here. |
| EDT-02 Upgrade verification | [Grid Hunt verify_save_upgrade.py](https://github.com/EdenP-Development/GridMates-Grid-Hunt/blob/feature/gh-v02-in-puzzle-map-look/scripts/verify_save_upgrade.py), 0ef751dd1251c2d1d62e2efa83def89b358aa539 | Fresh disposable emulator, old APK install, synthetic 11-map fixture, cold UI check, adb install -r, increasing version and exact maps before/after cold launch | Hardcoded QA package, baseline version 10345, UI strings and schema; adapt, never run on player phone. Require explicit emulator serial, timeout, certificate/hash checks in orchestration and explicit failure (avoid optimized Python asserts). Prior QA362 upgrade reported passed; latest current-head status not checked here. |
| EDT-03 Startup overlay | [Crossroads StartupBranding.kt](https://github.com/EdenP-Development/GridMates-Crossroads/blob/feature/identity-17-art-import/app/src/main/java/com/playereden/gridmates/crossroads/StartupBranding.kt), b50f933d3ee77dc17db3efea38a00e5808a797d7; [timing tests](https://github.com/EdenP-Development/GridMates-Crossroads/blob/feature/identity-17-art-import/app/src/test/java/com/playereden/gridmates/crossroads/StartupBrandingSpecTest.kt), 3c0247b20f7890d833abc340f3a0ca77f04ec5ea | Async decode, fallback, lifecycle, semantics, skip, 300/1500/300 per stage; Word Search draft adapts it | Follow branding/game-startup guide; timing still under physical review. Test stage race, focus/input, reduced motion and real wall time; no universal component claim. |
| EDT-04 Theme roles | [Sudoku GameTheme.kt](https://github.com/EdenP-Development/SudokuTogether/blob/main/app/src/main/java/com/playereden/sudokutogether/GameTheme.kt), 1722c22bb2334acb240eeac6c5840f102cc74fd8 | Compose Material3 centralized semantic colors, typography and shapes | Main light-theme reference only; adapt roles rather than palettes, test contrast and large text; EPS trust/security colors independent. |
| EDT-05 Seeded maze | [Sector Rebound web/game.js](https://github.com/EdenP-Development/Ricochet-Rumble/blob/main/web/game.js), 2d3d44595113d1582d4fb37689afa9fd14848051 | mazeRandom xorshift32; createMaze randomized depth-first spanning tree plus 16% braid chance for each eligible closed neighbor; adjacency and wall rectangles | Extract pure graph/geometry only if needed; validate positive dimensions, bounded size, symmetry/connectivity, repeatability and unchanged seed contracts. Not cryptographic RNG. |
| EDT-06 Arcade bot decisions | Same Sector Rebound blob | chooseBotObjective recovery/supply/evade/hold/reposition/engage; soloBotPursuitPoint remembers last observed target for bounded interval | Coupled to game state, geometry and balance. Adapt principles, not wholesale function; verify actual fairness and do not infer all modes use same perception. |
| EDT-07 Autonomous simulation AI | Private source review; details excluded | Reuse candidate | Design and test a separate generic implementation only when justified |
| EDT-08 Baseline integrity | Shared toolkit implementation | Read-only file fingerprint verification | No runtime acceptance claim |
| EDT-09 Asset packaging | [Word Search build.gradle.kts](https://github.com/EdenP-Development/GridMates-Word-Search/blob/feature/shared-startup-branding-2026-11-25/app/build.gradle.kts), 3b1506a1cb380c11ff9dc30ea1804212f876bc8f | pinned upstream startup assets, bounded download, SHA256 each build, offline cached build and local runtime asset source; existing preview-art build tasks | Draft CI pending; verify packaged bytes and release isolation before reuse. Rights and provenance distinct from checksums. |

## Deferred investigation
LAN transport, portable save/export implementation, Sudoku solver internals, Word Search generation/lexicon, procedural terrain, art/audio libraries, and Eden Comms protocol/security code not inspected deeply enough in this pass. Code search returned no matches for several queries; exact path reads recovered the above. Do not share signing keys, test credentials, real player data, security trust state, or unreviewed artwork. Eden Comms security design is not a general game networking library.

## Toolkit policy
Start with reference recipes, not a mandatory engine or package dependency. Prefer small pure functions, adapters at product boundaries, pinned versions, explicit rights and licenses, regression tests and consumer-specific acceptance. Each candidate graduates from source-inspected to isolated tested to consumer verified only with evidence. No automatic updates across apps. Do not publish extracted code until ownership and dependency terms verified under ASSET_LICENSING.md. No centralized SDK, telemetry, account or runtime network dependency.

## First proposed extraction
EDT-02/01: generalize safe QA upgrade verification and non-sensitive settings read patterns first, because they protect existing products. EDT-05: isolated seeded graph utility with repeatability/connectivity tests when a consumer needs it. EDT-07: simulation decision architecture with injected RNG and explicit trace; preserve original project source. EDT-03 remains shared branding reference rather than mandatory library. PORT-07 will establish lightweight review process.

This pass inspected actual source and selected test files, not executed CI or audited complete repositories. No app code, licenses, public releases or signing changed.

## EDT-02 v0.1 implementation checkpoint — 2026-11-25
[Read-only APK preflight](toolkit/edt-02/v0.1/README.md) implemented as new Python source; six local mocked/synthetic unit tests passed. Actual SDK/APK integration and disposable emulator upgrade harness remain pending. No consumer integration or release approval.

## EDT-02 v0.2 — receipt-bound candidate
[Version 0.2](toolkit/edt-02/v0.2/README.md) requires exact independently recorded hashes and versions, adds ZIP manifest presence check, ten unit test methods and real SDK synthetic signing fixture workflow. Tests authored; exact execution unverified. No device or save test yet; v0.1 preserved.

EDT-02 v0.2 integrated synthetic emulator job added (workflow commit 2b670f463ededbc5539dea8635c3389499352cdc). Preflight gates emulator job; actual install-over and synthetic file check designed, CI result unverified. No consumer integration yet.

## Local integrated Python regression — 2026-11-25
Python 3.13.5: `python -m unittest -v` and `python -O -m unittest -q` each passed all 15 tests using the actual preflight module (no stub). All four local source/test Git blob hashes matched repository files: preflight.py 914be34700be98c639a4a5c106ada51b558c6016; test_preflight.py e508e7b3ea7f5b42aef92167174516f3d2ac45b5; emulator_smoke.py 91818355c00c7a48cc390d3378e025a38b64143e; test_emulator_smoke.py 97aa966344dec86584a2b8ab815ed10b468f862e. These are mocked SDK/ADB tests only. No Android SDK executables on PATH; direct raw GitHub retrieval unavailable in local environment. Connected commit status/run queries returned empty (PR-filtered runs), not proof of workflow failure or success. Consumer pilot remains gated on actual SDK/emulator logs. No new runtime or workflow changes.

## EDT-01 v0.1 — independently tested candidate
[Safe preference reads](toolkit/edt-01/v0.1/README.md): original pure Kotlin read-only helper with explicit valid/missing/invalid status, strict types, range/option checks and defensive set copies. Actual local Kotlin/JVM 14/14 tests passed; committed source/test blobs match. Android adapter and consumer verification pending. Non-sensitive settings only; no automatic save repair or migration.

## EDT-01 v0.2 candidate
[Android adapter and expanded snapshot API](toolkit/edt-01/v0.2/README.md) authored; 26 JVM test cases pending execution, Android compilation/instrumentation pending. No consumer changes.

## Verified local regression — 2026-11-25
Actual kotlinc compilation and JVM execution passed all 26 tests. Local Git blob hashes matched committed SafePreferences.kt d3dd262f98e0976bd4b56abd382b676360acf8d2 and SafePreferencesTest.kt e6b1854c98987aa1c0980f79d829d2048648e4ec. Android SDK/adapter instrumentation and consumer integration not verified.

## EDT-08 v0.1 — verified baseline utility
[Read-only baseline verifier](toolkit/edt-08/v0.1/README.md) implemented as original standard-library Python. Twelve local tests passed in standard and optimized modes; exact committed blobs verified. Requires trusted independently recorded manifest and stable local directory; verifies listed bytes only. No consumer integration, runtime verification or release acceptance.

## EDT-09 v0.1 — verified archive intake
[Read-only asset archive verifier](toolkit/edt-09/v0.1/README.md) implemented; 14/14 local synthetic tests passed in normal and optimized Python, exact committed blobs matched. Requires trusted archive/member receipt; bounded ZIP verification, no extraction or image decoding. Real archive integration, image contract and runtime packaging gates remain pending.

## EDT-09 v0.2 — image contract candidate
[Image verifier](toolkit/edt-09/v0.2/README.md) implemented with Pillow 12.3.0; 12/12 real-decoder synthetic tests passed locally in normal and optimized Python, exact committed blobs matched. GridMates nominal bounds/color examples documented. No actual product icon, XML resource, archive extraction, CI or package acceptance verified. v0.1 retained.

## EDT-09 v0.3 — controlled staging candidate
[Controlled staging](toolkit/edt-09/v0.3/README.md) integrates exact sibling v0.1/v0.2 modules, explicit image selections, exclusive new output directory and staged manifest. 12/12 local synthetic integration tests passed normal and optimized Python; exact committed blobs matched. No real artwork, CI, project import or packaged APK verified. Next consumer-specific packaged resource verification.

## EDT-09 v0.4 — packaged asset verifier
[Packaged asset byte verification](toolkit/edt-09/v0.4/README.md) implemented. Actual local Python normal and optimized runs each passed 10/10 synthetic APK-shaped ZIP tests; committed source/test blob hashes matched. Checks required byte-preserved assets/ members and optional exclusive prefixes against independently recorded receipts. Actual signed APK, compiled res/ resources, runtime and consumer acceptance unverified. No application changes.

Visibility correction (2026-11-25): current public document excludes identified private-project details. Earlier Git revisions may retain them; no history rewrite or repository visibility change performed.

## Toolkit checkpoint — 2026-11-25
See [current toolkit verification and recovery checkpoint](toolkit/EDT_CHECKPOINT_2026-11-25.md) for implemented versions, recorded local tests, real historical Sudoku QA artwork byte verification and remaining consumer gates. No release promotion implied.

## EDT-09 v0.5 — executed drawable pilot
[Version 0.5](toolkit/edt-09/v0.5/README.md) adds explicit byte-preserved PNG drawable mapping, separate from v0.4. Actual local Python normal and optimized runs passed 8/8 tests; exact committed blobs matched. Executed on real historical Sudoku Visual 4 APK from artifact 14993249624: both master logo hashes matched; status mapped_drawable_bytes_match. No Android resource resolution, signature, current-head, CI adoption or runtime verification. No product changes. Next prioritize targeted consumer adoption and EDT-05 only when a consumer need is established.

## EDT-05 v0.1 — deterministic maze graph
[Version 0.1](toolkit/edt-05/v0.1/README.md) original standalone ES module with versioned seed contract, bounded dimensions, connected tree, straight preference and optional extra edges. Actual Node 22.16.0 14/14 tests passed; exact committed blobs match. Golden fixture established from observed initial implementation after correcting guessed expectation. No browser, Android, consumer or multiplayer verification; no existing generation behavior modified. Cumulative recorded local cases now 123, of which 14 executed in this checkpoint. Test counts do not establish readiness.

## EDT-05 v0.2 — graph analysis checkpoint
[Analysis and pathfinding](toolkit/edt-05/v0.2/README.md): exact v0.1 generator 14/14 rerun; v0.2 12/12 passed in Node 22.16.0. Committed blobs match local tested bytes. Cumulative current toolkit test count 135 (109 previously recorded plus 26 EDT-05 cases; no double counting reruns). No product changes or consumer acceptance. Frozen maze-v1 seed contract retained.

## Verified EDT-05 v0.1 checkpoint
Node.js 22.16.0: 14/14 tests passed; exact source and test blobs 0d79ae47c1d3db7ce706d11edb1acbb454d9c831 and 1a7561e4fe4603f8c141c5193ab35729b48b05ba matched. 300 seeded configurations plus maximum grid and golden fixture. No consumer integration. Preserve maze-v1 algorithm and all configuration fields; new behavior requires new version. This is a v0.1 regression rerun, not additional coverage. Latest recorded cumulative count remains 135 including v0.2; v0.2 was not rerun in this checkpoint.

## EDT-06 v0.1 — Arcade objective selection
[Original decision engine](toolkit/edt-06/v0.1/README.md) implemented and locally executed: Node 22.16.0 14/14 tests passed, including 108 scenarios; exact committed blobs match. Deterministic eligibility/scoring, critical health override and trace. Provisional weights; active actor lifecycle, perception, movement and balancing external. No consumer integration. Cumulative recorded toolkit cases 149 (135 previously recorded plus 14 newly executed). Next objective persistence and perception adapter; no product changes.

## EDT-06 v0.2 — Objective persistence and perception memory
[Controller](toolkit/edt-06/v0.2/README.md) implemented and tested. Actual Node 22.16.0 combined suite 28/28 passed (14 prior rerun plus 14 new); exact committed source/test blobs match. Score-margin hysteresis, emergency override, eligibility recheck, tick-bounded last observed position independent of engagement permission. No consumer integration, target identity tracking or actual perception/balance verification. Cumulative recorded toolkit cases 163 (149 prior plus 14 new). No product changes.

## EDT-07 v0.1 — Autonomous simulation utility selection
[Original generic selector](toolkit/edt-07/v0.1/README.md) implemented: actual Node.js 22.16.0 local tests 15/15 passed, including 192 scenario combinations; exact committed source/test blobs match. Normalized needs and personality, explicit task availability, survival priority and score trace. No private source copied, no learning, reservations, time progression or actual world execution. Emergency priorities override risk penalties, so callers must exclude unsafe tasks. No consumer integration or product changes. Cumulative recorded toolkit cases 178 (163 previously recorded plus 15 new); prior suites not rerun here. Next deterministic task reservations and conflict resolution.

## EDT-07 v0.2 — Task reservations
[Reservation module](toolkit/edt-07/v0.2/README.md) implemented; actual Node 22.16.0 18/18 tests passed, exact committed blobs matched. 500 requests for 50 tasks produced 50 unique owners and order-independent results. Single authoritative caller, one active claim per agent, tick expiry, owner release, renewal and deterministic priority. No fairness, distributed synchronization, world execution or consumer acceptance. Cumulative recorded cases 196 (178 prior plus 18 new); earlier suites not rerun. Next separate experience/learning module. No product changes.

## EDT-07 v0.3 — Bounded learning
[Learning module](toolkit/edt-07/v0.3/README.md) implemented; actual Node 22.16.0 13/13 tests passed, exact committed source/test blobs matched. Independent mastery/familiarity, success/failure gains, diminishing returns, 128 skills and 10,000-event progression tested. Integer rounding can plateau below cap; no preference coupling, fractional credit, consumer or balance verification. Cumulative recorded cases 209 (196 prior plus 13 new); prior suites not rerun. Next bounded outcome memory and skill-to-utility adapter. No product changes.

## EDT-07 v0.4 — Individual outcome memory and experience-informed decisions
[Memory and scoring adapter](toolkit/edt-07/v0.4/README.md) implemented. Actual Node 22.16.0 combined suite 29/29 passed (13 prior learning rerun plus 16 new); exact committed source/test blobs matched. Bounded 64-event history, tick expiry, task/kind matching, explicit skill mapping, bounded ordinary-task utility adjustment; survival scores/priority and eligibility unchanged. No spatial memory, confidence weighting, population or consumer integration. Cumulative recorded toolkit cases 225 (209 prior plus 16 new). Next v0.5 integrated synthetic population harness. No product changes.

## EDT-07 v0.5 — Integrated synthetic population experiment
[Population fixture](toolkit/edt-07/v0.5/README.md) implemented; actual Node 22.16.0 11/11 integration tests passed; four dependency source hashes and new committed source/test hashes matched. Seed42 scenarios 12 agents/100 ticks and 100 agents/200 ticks exposed severe meal-access contention and denied-task idling; larger scenario ends with 208 food but 89 critically hungry agents, both scenarios zero work completions. No survival/balance or consumer acceptance. Cumulative recorded cases 236 (225 prior plus 11 new); prior suites not rerun. Next v0.6 capacity, fallback and fairness comparison against frozen fixture. No product changes.

## EDT-07 v0.6 — Capacity-aware allocator (partial)
[Single-tick allocator](toolkit/edt-07/v0.6/README.md) implemented; actual Node 22.16.0 9/9 passed and exact committed blobs matched. Controlled 100-agent fixture: 12 meals, 30 fallback work assignments, 58 unassigned. Capacity constraints, eligibility filtering contract, priority/wait/score ordering and deterministic fallback; no persistent reservation replacement. Cumulative recorded cases 245 (236 prior plus 9 new); prior suites not rerun. Multi-cycle integration, explicit wait accounting, fairness and identical seeded baseline comparison pending. No product changes.

## EDT-07 v0.6 — Population integration checkpoint
Separate capacity-aware population fixture now implemented and executed. Node 22.16.0 combined allocator/population suite 16/16 passed (9 reruns, 7 new). Exact local dependency hashes matched v0.1 decision f4d8cedca9da2c5ef083a7cbe6b40a7eb55fb015, v0.3 learning 0b428996bdea100d02e5f5c0e3c868b66b14d270, v0.4 memory a67b35c75773ee9c7b25967cdb7a1afbf3c84c6f and v0.6 allocator 7fa341fa11636f16b5364154b30ca5f1a391b209. New population.mjs 7cb3de2f59124fe7d85e8327d298f33340981123 and population.test.mjs 804a295906cbb19fcfdb909975a21ae21534c1eb matched exact committed readback. Cumulative recorded cases 252 (245 prior plus 7 new). Earlier baseline not rerun; comparison uses recorded v0.5 values and fresh v0.6 execution.

Seed 42, initial food 12, meal capacity 12 bounded by start-of-tick stock, one field/workshop/trail slot, private bed per agent. Identical initial agent RNG and needs progression to v0.5; new allocation replaces one-tick reservation fixture only. Wait increments on denied first choice (even successful fallback), resets otherwise; no per-task waiting or fairness guarantee. Eligible alternatives must beat idle under original tie rules. One action per agent; gathering adds two food, eating consumes one. No borrowing against same-tick production.

| Metric | 12 agents / 100 ticks | 100 agents / 200 ticks |
|---|---:|---:|
| Eat | 210 | 410 |
| Rest | 690 | 18990 |
| Gather | 100 | 200 |
| Work | 100 | 200 |
| Explore | 100 | 200 |
| Idle | 0 | 0 |
| First-choice denials / fallback assignments | 962 | 19562 |
| Final food | 2 | 2 |
| Critical hunger agent-ticks | 0 | 14376 |
| Final critically hungry agents | 0 | 78 |

Behavioral blockers: food production capped at two units/tick; large settlement remains severely hungry despite improved access. Excessive rest (even at zero fatigue) masks idleness, first-choice denial is not eliminated, and no fairness guarantee. Next experiment: parameterize gathering capacity and gate unnecessary rest, measure meaningful activity and unmet need, separate changes through ablations. No actual game economy, performance certification, consumer integration or product changes. Preserve frozen prior versions.

## Scope checkpoint — shared development foundation (2026-11-26)
Purpose: reduce repeated work and improve existing product development/release reliability, not develop an unsolicited new game or mandatory universal engine. EDT-07 v0.1–v0.6 remain reusable experimental candidates; population fixtures are synthetic integration laboratories, not a product, economy design or gameplay balance target. Preserve recorded behavioral blockers (food throughput, unnecessary rest, waiting fairness) without treating them as release blockers for unrelated games. Proposed scope correction: defer v0.7 economy tuning until a named consumer has a demonstrated need and acceptance criteria. Prioritize reviewing toolkit adoption evidence and practical current-product needs (safe upgrades, asset integrity, branding, audio acceptance and project recovery); then select one bounded consumer pilot in coordination with its active branch/handoff. No automatic adoption, new game, release or package/signing changes. Recorded cumulative test count remains 252; no tests executed or runtime changes in this documentation checkpoint. Further simulation research remains optional, not canceled.
