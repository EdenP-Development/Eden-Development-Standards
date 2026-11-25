# Shared game startup v1.0 — owner-approved visual standard

Owner approved physical Sudoku Beta 3 Visual Review 4 presentation and nominal timing on 2026-11-24 (US local date). Adoption is authorized at normal development milestones, not automatic publication. EPS remains a separate pilot.

## Visual contract
Spudacus → GridMates → existing game menu for series titles. Standalone games use Spudacus only. Exact v1.0 assets, warm cream #FAE7CD, centered aspect-fit, no extra wording or sound. Each stage: 250 ms fade in, 1000 ms hold, 250 ms fade out; nominal 1500 ms per stage, 3000 ms for both at normal animation scale. Tap anywhere or Back skips the entire remainder. Respect reduced motion (pilot skips if animators disabled), avoid replay on rotation/resume, bundle offline, avoid redundant native splash or unnecessary initialization delays. Preserve product title, launcher identity, package IDs, signing and saves.

## Pinned assets
- Spudacus: https://github.com/EdenP-Development/Eden-Development-Standards/blob/015645bffb612e0f4311ec5a2d29e9c8bad91289/branding/spudacus/v1.0/full-transparent.png — SHA-256 74773dbda822161f73a639f959e8bce5c6e0b333a94ebeb8ee27f620d4995d25
- GridMates: https://github.com/EdenP-Development/Eden-Development-Standards/blob/9affedc94ca5a6b896d36148f46f14a4e8218c3a/branding/gridmates/v1.0/runtime-transparent.png — SHA-256 eef6d631cac0b9523f7e0dbebac229f9a2458d36fe2e73e111d251704d9ff292

## Reference implementation
[Archived exact Kotlin source](reference/StartupBranding.kt) is copied from SudokuTogether at 96747991e98f78c90e10d6eda447d1be085a3674. It is a reference, not a drop-in library or independently validated component. For Compose, adapt package and drawable IDs; mount once over existing root, with showInitially = savedInstanceState == null and optional seriesDrawable (null for standalone). Pilot uses safeDrawingPadding, 24dp padding, max width 420dp, width fraction .82 and max height 260dp. For other engines port the behavior rather than importing Android code or adding Compose. Keep overlay lifecycle independent of game state. Preserve existing initialization; provide safe fallback for missing artwork, avoid input leaking to gameplay, and verify focus/semantics. Do not claim these improvements exist in the original reference.

## Pilot receipt
- [Approved source](https://github.com/EdenP-Development/SudokuTogether/commit/96747991e98f78c90e10d6eda447d1be085a3674)
- [Pilot documentation and owner receipt](https://github.com/EdenP-Development/SudokuTogether/blob/feat/beta3-foundation/docs/BETA3_STARTUP_PILOT.md)
- [Visual build](https://github.com/EdenP-Development/SudokuTogether/actions/runs/45550962814) and [Android gate](https://github.com/EdenP-Development/SudokuTogether/actions/runs/45550962759) reported passed in source receipt, both asset hashes passed. Instrumentation compiled, not executed. Owner physically approved portrait appearance and nominal timing; actual wall-clock startup time not measured. Pilot is a skippable timed overlay, not readiness-based. Skip, reduced motion, warm resume, rotation, offline behavior, accessibility focus, landscape, resource fallback and performance are not individually physically verified.

## Adoption
GridMates Word Search, Grid Hunt and Crossroads: two stages. Sector Rebound (Ricochet-Rumble): Spudacus only. Other titles: determine series membership from project handoff. Integrate on normal focused branches, verify exact asset hashes and packaging, test sequence and skip at both stages, reduced motion, rotation/resume, offline and fallback, accessibility, startup latency and gameplay/save regression. Run exact-head CI and produce internal QA if appropriate; record evidence and owner feedback in project handoff. No automatic releases, no mass package/signing changes. Track each project separately; approval of Sudoku visuals is not evidence of another game's integration.

