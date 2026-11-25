# PORT-05 — Development and release priorities

2026-11-25. Proposed management priorities based on PORT-02/04 evidence, not owner-approved publication order, delivery dates, market forecasts or commercial readiness scores. Product handoffs may be newer. Preserve individual product roadmaps and stricter gates.

## Work lanes
| Lane | Products | Purpose |
| --- | --- | --- |
| A — Protect and advance public beta | Sudoku | Maintain existing owner-reported Beta 2, verify downloadable bytes and durable archive, complete Beta 3 coach and physical review; no forced migration |
| B — First public beta candidates | Word Search, Sector Rebound | Consolidate existing development, not expand feature scope; each releases only after its own gates |
| C — Alpha maturation | Crossroads, Grid Hunt | Finish coherent playable loops, visual/accessibility and save QA; promote only when stable |
| D — Security-gated development | Eden Comms | Continue usability/reliability work and independent security preparation; no public functional beta until charter gates pass |
| E — Preserve and selectively resume | Private project tracking | Preserve exact baselines; reconcile current refs privately |
| F — Research / unclassified | Unclassified projects | No release commitment; classify in appropriate access-controlled contexts |

EPD is a separate business workstream; storefront inventory and visual identity remain open. Do not assume older games are abandoned or unpublished.

## Proposed near-term beta sequence (not binding)
1. Sudoku: protect existing Beta 2 first; then finish integrated Beta 3, coach proof/teaching, gameplay and startup review, save/upgrade and publication receipts. Legacy signer issue remains separate from successor channel.
2. Word Search: reconcile signed beta 124 and newer development/versionCode; review startup PR 200, launcher, library/album progress, signed upgrade and physical acceptance. Candidate for next new public beta, not a declaration that it is ready.
3. Sector Rebound: complete current R2/R3 refinement and selective draft consolidation, actual private beta APK, save/upgrade, two-phone LAN and match balance decisions. No bulk merge or public upload.
4. Crossroads and Grid Hunt: parallel alpha maturation; order based on accepted coherent gameplay and evidence, not branding polish. Crossroads authoritative handoff and signer reconciliation; Grid Hunt latest combined CI, upgrade, map clarity and consolidated phone review.
5. Eden Comms has an independent security lane, not a lower-value product. Physical 54-case matrix, independent review and release engineering remain hard gates; cosmetics cannot substitute. Internal QA only until qualified.

## Two release tracks
Public beta: freeze advertised usable scope; verify rights/privacy, exact signer/package/version/artifact, applicable install-over and save/export, core gameplay/physical evidence, support route and honest limitations, archive and owner authorization. Free or optional donations preferred per BUS-01; no automatic publication.

Commercial: separate scope/quality acceptance under BUS-04, all mandatory security/rights/privacy gates, verified customer value, support/maintenance, pricing and entitlement plan; choose storefront and verify live requirements. Google Play is long-term and requires BUS-05 recheck, not a deadline. Do not add monetization SDKs just to prepare. Sudoku and Word Search are reasonable first commercial *evaluation* candidates based on current documented development maturity, not proven market demand or readiness. No fixed prices or paid release dates.

## Shared corrective queue
P0 before next distribution: owner-controlled independent signer recovery drill (private; record only status/date and fingerprint match), preserve current installs and accepted APKs, reconcile signing/versions against exact receipts, verify durable archives and public downloads where applicable.
P1: finish current combined CI and real phone acceptance; group coherent changes into consolidated review builds; preserve existing data and test actual compatible install-over. Reuse synthetic fixtures; never uninstall to bypass mismatch.
P2: per-product rights/data inventories, honest listing/FAQ, support route, accessibility and performance; complete before relevant release gate, not after.
P3: investigate reuse and technical debt; prioritize proven bottlenecks and maintenance, not speculative platform rewrites.

## Capacity policy
Proposed operating rhythm: one coherent next milestone per active product, limit concurrent review builds to what owner can actually test; do not start more public-beta candidates when existing releases need urgent repair. Use active handoff as task source, exact-head CI as evidence, owner feedback as acceptance; finish review before superseding runs unless a concrete defect needs correction. Keep old projects recoverable without forcing active work on every title. No imposed weekly hours, fixed percentages, or automatic schedules.

## Decision rules
Release order can change as gates clear, owner feedback arrives, or critical defects emerge. Rank by existing customer impact, blocker severity, product completeness, evidence quality and remaining work, not counts of tests or cosmetic features. No numerical score can override mandatory gate. All publishing, paid pricing, signer changes, account setup and retirement require explicit owner decisions. No app code or release actions in PORT-05.

References: PORTFOLIO_REGISTRY.md, PORTFOLIO_STANDARDS_ADOPTION.md, PORTFOLIO_BRANDING_ADOPTION.md, APP_REGISTRY.json, MONETIZATION_STRATEGY.md, COMMERCIAL_READINESS.md, GOOGLE_PLAY_READINESS.md, RELEASE_CHECKLIST.md. Next PORT-06: verify actual reusable source/tests and licensing boundaries before proposing shared components.

Visibility correction (2026-11-25): current public document excludes identified private-project details. Earlier Git revisions may retain them; no history rewrite or repository visibility change performed.
