# Public website maintenance contract

For all Eden Practical project chats. Product development remains independent; the website is an evergreen public directory, not a live CI dashboard.

## When to update
Public release, changed availability, new platform, approved public artwork, material changes to advertised features or support/privacy terms. Internal QA, refactors, draft branches and experimental features do not require website edits.

## Release handoff
Record product name, public channel and exact URL, public release stage, supported platform, release receipt, date verified, approved artwork source and any changed privacy/support information in the product handoff. Send a concise update to the central portfolio registry. Verify actual storefront availability; do not infer it from a GitHub tag or signed QA artifact. Keep private source and unpublished details out of public records.

## Website maintenance
Read website/CONTINUE_HERE.md and fresh main in EdenP-Development/Eden-Development-Standards. Edit website/public only. Keep unrelated concurrent changes; use current parent/tree and compare-and-swap ref update, retry by rereading on conflict. Preserve noindex until launch acceptance. Use stable URLs and broad labels, no internal build numbers. Verify changed local references and actual Cloudflare production revision after commit. Record evidence and limitations in website handoff. No app/storefront publication is authorized by this procedure.

## Curation
Rovers of Fortune is explicitly excluded by owner direction. Public listing alone does not warrant inclusion. New projects need public suitability and owner direction; existing private repositories are not an obstacle to accurate coverage of already public games.

## Public integrity verification
Before publication run `python -m unittest discover -s website/qa -v` and `python website/qa/audit_public.py`. Review exact-revision Public website integrity CI. This is detection only; automatic Cloudflare deployment is independent. Deliberately revise prelaunch checks at authorized indexing activation.

## Privacy handoff
Use [portfolio privacy readiness](PRODUCT_PRIVACY_READINESS.md) for public-safe release coordination and the existing project data-handling template for detailed evidence. Product notices require exact distributed-release verification and owner approval before publication.

## PORT-WEB-20 — Scope alignment (2026-11-28)
Product teams own exact release evidence and proportionate QA; the website consumes verified handoffs and approved notices. Existing drafts and browser harness retained; further harness expansion deferred until a real product need. Do not treat all portfolio privacy reviews as a blanket website indexing prerequisite; actual applicable privacy/support requirements and owner approval remain mandatory. Follow the practical closeout in website/CONTINUE_HERE.md. No policy approval or publication authorized.
