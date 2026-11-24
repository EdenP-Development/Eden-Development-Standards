# EdenP Development — practical itch.io publishing guide

Established from GridMates: Sudoku Beta 2, November 24, 2026. Apply proportionately to each game; do not copy Sudoku-specific features, keys, permissions, branding or claims.

## 1. Before publishing
- Read the project's current handoff and shared RELEASE_POLICY.md, RELEASE_CHECKLIST.md, SIGNING_KEY_MANAGEMENT.md and SAVE_PRESERVATION.md.
- Confirm distribution channel, stable package and certificate, version, exact source, APK checksum and receipt; run appropriate automated and physical QA. Record actual failures, limits and owner-approved deferrals.
- Preserve existing player progress. If package/signing identity must change, test a portable transfer and tell players to keep the old installation until progress is verified. Never quietly replace signing identities.
- Obtain owner acceptance. Preserve exact accepted bytes in a durable archive, not just an expiring Actions artifact. Keep signing credentials private.
- Rename the accepted APK to a clean public filename such as GameName-Beta2.apk without changing its bytes. Do not distribute internal receipts, QA labels, secrets or personal data.

## 2. Create or update itch project
- Owner handles account-only publishing operations; assistant prepares files, copy, artwork and verification.
- Use a recognizable title, short tagline, downloadable project classification, correct platform, genre and accurate tags. Choose pricing, status and comments with owner. Do not assume all projects are free or Android.
- Upload accepted APK, select Android where applicable, preserve or hide legacy downloads deliberately; no accidental deletion.
- Provide copy-ready evergreen HTML for description AND separate download/install instructions. Use simple headings, paragraphs and lists. Explain actual features, platform requirements, networking limits, support and backup/update advice. No dates, version numbers, changing feature counts or unimplemented promises. Specific migration instructions belong in release notes.
- Disclose AI use honestly using itch's applicable categories and a short natural statement; verify actual programming, graphics, audio and text use for each project. Do not erase the owner's design/testing contribution.
- Use accurate app-specific privacy disclosures, asset licenses and third-party attribution; do not publish unverified boilerplate.
- Save and preview the formatted HTML. If body validation says expected text between 1 and 204800 characters, check that pasted content appears in normal editor mode; use a shorter plain-text or simple HTML draft if necessary.

## 3. Evergreen art kit
Keep an approved master and upload export for each asset; record source, approval, dimensions, SHA-256, license/provenance and intended role in the game repo. No version/date/count text in permanent art. Dimensions below are suggested exports except explicit aspect requirements observed in itch editor; recheck live UI before future publication.

| Asset | Export target | Purpose |
| --- | --- | --- |
| Main cover | 630x500 (5:4 approximately) | Listing thumbnail |
| Actual screenshots | Native resolution, crop only system bars | Factual gameplay evidence |
| Feature panels | 1080x1350 suggested | Readable promotional highlights |
| Social share | 1200x630 suggested | Link previews |
| Wide cover | 1680x720, 21:9 | Special featuring |
| Favicon | Square PNG, 512x512 master | Browser tab; test 16/32 px |
| Logo | Wide transparent PNG | Promotional overlay; test light/dark backgrounds |
| Devlog cover | 1600x900 suggested, 16:9 | Release-specific announcement |
| Android launcher icon | Adaptive foreground/background plus legacy exports | In-game distribution, separate from storefront |

Use actual screenshots, not regenerated interface images, for claims of gameplay. Crop pixel-exactly without generative editing; do not reconstruct text or invent UI. AI-assisted illustrations and mockups must be understood as promotional, not raw screenshots. Keep individual visual identities, coherent series branding and approved art. Verify text, transparency, aspect ratio, small-size legibility, Android adaptive masks and thumbnail crops. No need for a full redesign each release.

## 4. Devlog
- Short, human first-person writing, not corporate marketing. Explain origin or motivation where relevant, verified changes since previous public version, important install/migration instructions, future ideas clearly marked and invitation for feedback. Be transparent about AI assistance without dismissing the owner's work.
- Provide title and copy-ready HTML. For substantial updates choose Major Update or Launch if appropriate. Attach accepted build and relevant promotional images, add accurate tags/language, enable comments if desired. Version-specific counts and release label are fine here.
- Upload a 16:9 cover, preview, then owner publishes. Do not publish without authorization.

## 5. Verify and close
- Open public project and devlog, check current copy, gallery, visibility, Android download and migration guidance. Download public APK and compare exact checksum where possible; distinguish owner-reported publication from independently verified page/download. Cached pages or unavailable tools are not proof of failure or success.
- Update README, CONTINUE_HERE, release handoff, distribution receipt/registry and shared APP_REGISTRY.json. Use fresh reads and compare-and-swap; preserve concurrent edits by other projects. Record public URLs, accepted source/build/signing fingerprint, archive location, deferred tests, approved artwork and next milestone.
- Promote reviewed source using normal PR/CI process; never silently merge unrelated work. Record unresolved archival or verification separately from actual publication.
- Resume development. No commercial Google Play process unless appropriate and requested.

## Reusable prompt for another project chat
Read this guide and the latest shared standards and your project's handoff. Audit the current public listing (if any), accepted build, signing identity and assets. Prepare a proportionate itch release kit: clean verified download, evergreen description and install HTML, authentic screenshots, matching evergreen branding, concise personal devlog and release-specific cover. Work one step at a time, preserve approved design and player progress, handle technical work yourself, involve the owner only for genuine decisions/account actions/testing, and checkpoint verified results in both repositories. Do not copy Sudoku's package ID, credentials, gameplay claims or artwork blindly.

## Reference pilot
GridMates: Sudoku: https://sir-spudacus.itch.io/gridmates-sudoku
Beta 2 devlog: https://sir-spudacus.itch.io/gridmates-sudoku/devlog/1804670/gridmates-sudoku-beta-2-growing-our-little-puzzle-game
Owner-reported publication; independent public download verification and durable archive remain pending. This guide is a reusable workflow, not a claim that every pilot gate was independently completed.
