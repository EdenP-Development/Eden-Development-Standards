# PORT-03 — Branding adoption and timing audit

2026-11-25. Scoped source and handoff review; not independent execution of CI or device tests. Preserve accepted artwork, product icons, signing and saves. No product implementation changes here.

| Product | Inspected ref / evidence | Nominal timing | Status / next action |
| --- | --- | --- | --- |
| Sudoku | feat/beta3-foundation StartupBranding.kt blob 54b5b5a0dcd387ff37ab02377d02af09402a265f; BETA3_STARTUP_PILOT.md | 250/1000/250 x2 | Historical owner acceptance; timing reopened; evaluate longer trial |
| Grid Hunt | feature/gh-v02-in-puzzle-map-look StartupBranding.kt blob 4297eb29d9c764bef9b281f9577969fe1e602a9e; GH-V36-H handoff | 300/1500/300 x2 | Adopted in active development per owner 2026-11-25; revised timing physical acceptance and fresh combined CI not established |
| Crossroads | feature/identity-17-art-import StartupBranding.kt blob 5a60f864e060cd8ca6e1a9f9de7b57d0ae0a836e; MainActivity mounts overlay; build script pins both hashes | 250/1000/250 x2 | Source integration verified on inspected branch; latest branch/device acceptance not established |
| Word Search | ci/word-search-beta-signing MainActivity.kt blob 26a57ea971c68920a99cd80ba688e8129acaa116 | Native Android splash only | Shared overlay not present in inspected entry point; other branches not checked; integrate through normal milestone if needed |
| Sector Rebound | main CONTINUE_HERE.md blob ca428fa203a797ad91ece62c7400351d49b309d8; PR 154 merge 756b9a7a61f57b6851a7b91223ef659dbd3a1f4a | 250/2000/250 x1 | Owner acceptance and integration reported; preserve local approved 2.5s; exact native implementation not retrieved |
| Eden Comms | main appearance/EpsStartup.kt blob 094947254815a6b10155ba9a53b7851187353e89; MainActivity mounts; pinned EPS build asset | 250/2500/250 x1 | Revised 3.0s source verified on main; exact revised signed APK and physical acceptance pending; EPS independent |
| Older games | PORT-01 inventory | Unknown | Defer until active development resumes |

## Candidate decision
Historical v1.0 remains valid; proposed v1.1 standalone 2.5s (already accepted locally in Sector Rebound), series 4.2s (Grid Hunt trial). EPS now implements 3.0s independent pilot, superseding proposed 2.5s. Owner confirms Grid Hunt and Sector Rebound adoption; adoption is distinct from physical timing acceptance. No global promotion without corresponding owner acceptance. Verify exact hashes, sequence, immediate skip, reduced motion, resume/rotation, offline, fallback, input/accessibility focus and startup overhead. Crossroads asynchronous decode and Grid Hunt fallback/semantics are reuse leads, not certified components. EPS content mounts after branding; evaluate initialization impact without touching security boundaries. Record exact artifact and source, actual physical feedback, automated test scope and limitations. No mass rollout or publication.
