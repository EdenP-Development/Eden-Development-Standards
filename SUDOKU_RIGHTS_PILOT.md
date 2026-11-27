# BIP-04 — Sudoku asset rights pilot (2026-11-27)
Planning/evidence inventory only. No legal clearance, license change, asset transfer or release approval. Follow ASSET_LICENSING.md and templates/ASSET_RIGHTS_REGISTER.md. Public metadata only.

## Inspected evidence
SudokuTogether active branch feat/beta3-foundation, CONTINUE_HERE.md blob 8b0521577f16a65ed43314fbc638c6df3d577b42; latest handoff reports runtime 023c250 quality/unsigned candidate success, physical and signed upgrade gates open. app/build.gradle.kts blob 6e6a15ac7b83449326a3f2bd429ac6d24f7f7a35; core/build.gradle.kts edcc88be29abf327d633cc06cfb5edffdde7670f. LICENSE and NOTICE root requests on active branch 404; not exhaustive. No exact APK inventory or resolved dependency graph inspected.

| Group | Evidence | Rights status / action |
| --- | --- | --- |
| Code and synthesis | Git history; docs/BETA3_MASTER_AUDIO_LIBRARY.md blob 1705eef136ab998f55cdbf9c7e98a61c123e6052 | Review pending: human contributions, AI assistance, external code, terms, six synthesized effects and reproducible exports. |
| Branding and promotions | docs/ITCH_PROMO_ASSETS.md blob 2e3bb36f1d5299dcf9855f495e0982037f762d75 | Review pending: retain exact art, provider/terms/input provenance and human edits; screen marks; illustrative UI not raw gameplay. |
| Collectibles and habitat art | active handoff and existing art manifests | Review pending: per-asset provenance and rights, distinguish historical and candidate assets. |
| Fox V1 emotes | active handoff, 12 stable IDs, checksum verification reported | Review pending: source rights separate from technical/visual approval. |
| Six Cozy Puzzle tracks | docs/BETA3_SOUNDTRACK_INVENTORY.md blob 4c5634c726066399ddd3a7e78e66473436a08d71; central audio/gridmates/library/v0.1/README.md | Review pending: owner-reported Suno Pro; six original/runtime fingerprints recorded, track-specific entitlement not established. Keep account evidence private. No new distribution while unresolved. |
| Fonts, vocabulary, puzzle data | not inventoried in this pass | Unknown: source and embedding/redistribution terms. |
| Third-party dependencies | Gradle declarations below | Review pending: exact versions, resolved graph, license texts, NOTICE and packaged obligations. |

## Direct production dependency declarations
Internal :core; androidx.core:core-ktx 1.15.0; androidx.activity:activity-compose 1.10.1; androidx.lifecycle:lifecycle-viewmodel-compose and lifecycle-runtime-compose 2.9.0; kotlinx-coroutines-android 1.10.2; kotlinx-serialization-json 1.8.1 (also core); Compose BOM 2025.04.01; compose UI, UI tooling preview, material3 versions managed by BOM. Separate debug/test dependencies exist; verify actual packaging, do not assume test dependencies shipped. Resolve releaseRuntimeClasspath for exact candidate; inventory transitive artifacts and applicable license/NOTICE files, then inspect APK. No blanket Apache clearance inferred.

## Music entitlement
Suno help https://help.suno.com/en/articles/2410177 and https://help.suno.com/en/articles/9601665 describe paid-plan commercial rights; https://help.suno.com/en/articles/2425729 warns against assuming retroactive rights. Verify exact applicable terms at creation/download, plan dates and remix/extension/input status for each track (cozy-01 through cozy-06). Commercial permission is not copyright registration or exclusivity. Keep receipts and song IDs in private evidence storage; public register records status only.

## Candidate notice for owner review (not adopted)
"GridMates: Sudoku is developed by Spudacus. Copyright in qualifying original human-authored material is reserved by its respective rights holders. Third-party components remain subject to their respective licenses. AI-assisted material is subject to applicable rights and terms." Confirm actual holder/year and exact license scope before adoption; do not override MIT or third-party grants, or imply LLC ownership.

## Next gate
Obtain track evidence, resolved dependency graph and notices, release-specific asset manifest and contributor/AI provenance; reconcile exact packaged inventory before public beta or paid distribution. Existing release concerns triaged separately. Reuse this lightweight process per product; no automatic notices or code changes.
