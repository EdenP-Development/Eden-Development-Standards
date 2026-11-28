# PORT-WEB-15 — Portfolio privacy readiness register

Baseline 2026-11-28. Coordination record only, not a privacy policy, product data inventory, compliance finding or release authority. Covers the curated public website portfolio. Product repositories retain exact-release evidence; this register records safe public summaries and evidence status only. Do not copy private implementation details, sensitive security findings, credentials or customer data into this public repository.

## Readiness snapshot

| Product | Website availability label | Product notice readiness | Next evidence request |
| --- | --- | --- | --- |
| GridMates: Sudoku | Public Android beta | Separate Beta 2 and Beta 3 drafts; neither approved | Verify delivered itch APK and reconcile release identity; exact data inventory, publisher/contact and audience |
| The Last Taters | Public browser alpha | Initial source reviewed; unpublished notice candidate staged | Exact itch artifact, runtime network/storage verification, contact and audience |
| Operation Phosphor | Public browser game | Initial source reviewed; unpublished notice candidate staged | Exact itch artifact, runtime network/storage verification, contact and audience |
| GridMates: Word Search | In development | Not assessed in this register | Release-specific data inventory, storage, permissions and runtime |
| GridMates: Grid Hunt | In development | Not assessed in this register | Release-specific data inventory, storage, permissions and runtime |
| GridMates: Crossroads | In development (website label) | Unpublished Beta 1 draft staged; not independently assessed here | Reconcile frozen release evidence and owner approval; see website/drafts/crossroads-beta1-privacy.md |
| Sector Rebound | In development | Not assessed in this register | Release-specific data inventory, peer transfers, player information and controls |
| Eden Comms | Experimental | Not assessed in this register; stricter charter applies | Exact release evidence and independent security/physical acceptance under project charter |

Availability labels reflect the website, not a fresh storefront audit. Unknown means unreviewed here, not absent or unsafe. Rovers of Fortune excluded by owner direction; designs storefronts require separate review if activated.

## Evidence states

Unknown / Draft / Source reviewed / Exact artifact verified within stated scope / Owner approved / Published and URL verified / Blocked. Record separate states for data inventory, runtime behavior, notice and storefront declarations; do not collapse them into a compliance score. A material release change reopens affected evidence.

## Product handoff (copy into the product's existing release record)

- Product, channel, exact release/build and verification date:
- Data handling register reference (use existing templates/DATA_HANDLING_REGISTER.md):
- Packaged artifact, manifest/dependency and runtime evidence status:
- Local storage, peer/network exchange, retention and user controls reviewed:
- Audience, platform disclosure and publisher/contact status:
- Notice revision and approved public URL (if any):
- Material changes since previous approved notice:
- Remaining gates and next owner action:
- Evidence access: public-safe summary only; keep restricted evidence in product's authorized context.

## Website publication procedure

Use PRIVACY_STANDARDS.md, GOOGLE_PLAY_READINESS.md and website/PUBLIC_UPDATE_CONTRACT.md. Read latest product handoff; review current applicable official store requirements at release. Confirm exact distributed behavior, actual publisher, monitored private contact, applicable audience/rights obligations and effective date. Obtain owner approval before publishing a product policy. Keep historical versions by release/channel; test stable HTTPS URL and update site validation and sitemap where appropriate. Do not substitute newer draft for older public build. Product team owns in-app and storefront links; this register does not authorize their modification.

## Current shared gates

Dedicated monitored contact not confirmed; product policy approval remains open. Existing general website privacy information is separate from app notices. Sudoku Beta 2/Beta 3 drafts are in website/drafts. Browser product privacy assessments are prioritized because already publicly playable; Android release-specific evidence remains mandatory. No indexing activation or public notice publication authorized here.

## PORT-WEB-16 — Browser source triage (2026-11-28)

- The Last Taters: documented public baseline Alpha 0.10.1; initial review of main index and game script found local progress, profile, preferences, save slots, backups and slot deletion. No direct network API hits in initial script scan. Exact delivered artifact and runtime not verified.
- Operation Phosphor: README identifies RC8 as browser distribution source; initial review of self-contained HTML found local progress, configuration, statistics, unlocks, backup and synchronization metadata. Local split-screen documented. Android Play Games foundation is distinct; no direct network API hits in initial HTML scan, but bridge behavior and exact delivered runtime remain unverified.
- Crossroads: parallel product workflow staged a Beta 1 draft; do not treat staging as approval or independent verification.
- Next: obtain exact distributed browser packages or reliable release receipts, inspect complete asset/dependency sets, exercise browser runtime storage/network and deletion controls, distinguish itch hosting from game behavior, and confirm publisher/contact/audience before drafting approval candidates. No claim of zero data collection or compliance. No public notice, hosting, indexing or product change.

## PORT-WEB-17 — Browser notice candidates (2026-11-28)
Both documented public baselines (Taters Alpha 0.10.1, Phosphor RC8) have unpublished candidates in website/drafts/the-last-taters-browser-privacy.md and website/drafts/operation-phosphor-browser-privacy.md. Both files read back successfully. Neither repository listed GitHub release assets; exact itch packages and runtime behavior remain unverified. Taters newer release branches are not evidence of public behavior. Next obtain distributed archives/receipts, verify runtime and dependencies, confirm monitored contact, audience, publisher and effective dates, then request approval. No live website, app, storefront or indexing changes.

## PORT-WEB-18 — Browser privacy verification procedure (2026-11-28)
Shared procedure at [website/qa/BROWSER_PRIVACY_VERIFICATION.md](qa/BROWSER_PRIVACY_VERIFICATION.md), committed 92cb42a00a0b23a469ac1d358fe3908e9f3b8026. Defines exact release identity, static dependency review, controlled online/blocked egress and hosted embed observations, storage and deletion scenarios, sanitized receipts and approval gates. Taters Alpha 0.10.1 and Phosphor RC8 scenarios planned only. Existing website layout QA is not privacy verification. Next implement reusable isolated browser observation harness with synthetic regression fixtures, then run against authorized exact artifacts or explicitly labeled source baselines. No runtime audit executed, no policy approved, no product or public website changes; preserve noindex and staged sitemap.

## PORT-WEB-19 — Initial executable browser privacy harness (2026-11-28)
Added website/qa/browser_privacy.py, test_browser_privacy.py and .github/workflows/browser-privacy-fixtures.yml at commits 61dd6e3d57a4b501035a3a92ea9813c2a599a04a, c8aa9efe9cdddc1222de7b64f61d26585a4428a8 and b6b83fec900da4be86b84bd160d72dd18be21d68. Initial trusted-local blocked-egress harness counts storage entries, intercepts HTTP and WebSocket attempts, reports origins only and counts errors. Not an OS isolation boundary, online or hosted audit, nor proof of no traffic. Four synthetic tests authored; workflow 46127867769 in progress at inspection, no pass claimed. Next inspect actual fixture results and fix evidenced defects before product trials; add exact artifact identity and product-specific scenarios. No live site, product, policy, storefront or indexing changes.
