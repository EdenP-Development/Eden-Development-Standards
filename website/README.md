# Eden Practical website — deployment home

The existing hub is the canonical repository. No separate website repository is required.

- website/redesign/ contains the current development records and recovery tools.
- website/public/ will contain the actual deployable static site, and nothing else.
- Private V14 archive: search Drive for eden-practical-artwork-pilot-v14.zip. Its fingerprint is in redesign/review-recovery-v14.json.

Restore the existing candidate locally from the hub root:

    python website/redesign/review-patches/restore_site.py /path/to/eden-practical-artwork-pilot-v14.zip /path/to/new-review-directory

The command restores the 38 actual site files (13 HTML, CSS, 24 artwork) but not the receipt. The result is still the V14 review version; it is NOT a public release. It contains draft notices and noindex. Do not commit uncleared assets or deploy the restored review version automatically.

When the public content is ready, put the approved HTML/CSS/images in website/public/. For initial Cloudflare Pages Direct Upload, upload only that folder. For later Git integration, use the existing hub repository, no framework, repository root, no build command for committed static files, output directory website/public, production branch main and website/public/** build watch path where supported. Disable automatic deployment until the approved files exist. Verify the actual dashboard configuration; this is a proposed setup, not an existing integration.

No need for private staging for ordinary public-ready content. A public preview is public. Test the deployed links, HTTPS and mobile experience. No custom domain purchase is necessary for the initial setup.

## WEB-09.03B — Visitor-facing copy (2026-11-27)
Executed local refine_public_copy.py against exact V14 archive (38 input hashes passed); 48 literal replacements across 13 pages. V15 ZIP SHA-256 d9344d0a732131ab5d0f141d4466ae0d40d0852dea35754baabe7740f28c7fd9, 2308171 bytes. All 38 output payload hashes checked after ZIP readback; all href/src lists unchanged, 160 local refs passed, one external destination unchanged, CSS and 24 assets untouched. Generic pilot banners/title/footer wording removed while meaningful development disclosures retained; privacy and support remain drafts, no contact invented, noindex and publication_authorized=false retained. Reproduce with `python website/redesign/review-patches/refine_public_copy.py V14.zip V15.zip` (fresh destination; ZIP timestamps may differ). Local execution and Git readback are separate checks. V15 delivered in chat; no new browser run, public directory population or deployment. Next resolve actual artwork permission and public policy/contact decisions, populate website/public in existing hub and connect hosting. Avoid speculative tooling.

## WEB-09.03C — Actual V15 website source in hub (2026-11-27)
Stored exact 13 HTML pages and shared CSS in website/source/ from the verified V15 archive. Hub is public; 24 artwork binaries remain in private Drive pending distribution scope confirmation. Source retains review noindex and draft policy wording; not standalone without assets, not hosting output. V15 private backup uploaded, metadata shared=false, raw retrieval succeeded; recovered archive matches prior SHA-256 d9344d0a732131ab5d0f141d4466ae0d40d0852dea35754baabe7740f28c7fd9, 2308171 bytes, exact entries and 38/38 payload hashes. Next confirm artwork use and public contact details, then populate complete website/public and connect hosting. No new repository, host or deployment.

## WEB-09.03D — Complete artwork integration
Owner explicitly approved public use of all 24 promotional assets and storage in the public hub, subject to applicable third-party rights. V15 archive SHA-256 d9344d0a732131ab5d0f141d4466ae0d40d0852dea35754baabe7740f28c7fd9 and 38 payload hashes verified locally. Uploaded all 24 original asset bytes in two batches; Git blob fingerprints matched independently calculated local fingerprints. Complete website/source now contains 13 HTML pages, CSS and 24 images. No claim of blanket third-party rights certification. Existing recovery archive remains unchanged. Next finalize public privacy/support wording and hosting; no new repository or deployment.

## WEB-09.03E — Complete deployment directory (2026-11-27)
Created website/public/ from complete V15 source: 13 HTML pages, shared CSS, 24 artwork files. Updated only index.html, privacy.html and support.html wording to present factual visitor information, not an effective app policy or active support contact. Original V15 source unchanged. Static scan of exact candidate: 160 local href/src references including anchors resolved, one existing external itch.io destination retained, one h1 per page, noindex,nofollow retained on all 13 pages until launch. Output contains exactly 38 files; no README, receipts, private archives or QA tools. This directory is now ready for host configuration and preview, not an approved final public launch; no Cloudflare project, deployment or new browser run. Dedicated contact and product-specific notices remain pending; no fabricated details. Next connect Cloudflare Pages to existing hub with output website/public, then test actual hosted site and remove noindex when ready. No separate repository or additional infrastructure.
