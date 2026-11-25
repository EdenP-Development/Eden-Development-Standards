# PORT-07 — Lightweight portfolio review and recovery process

2026-11-25. Proposed operating process for Eden Practical, Spudacus, GridMates, EPS and EPD. Keep individual projects autonomous; central standards are the coordination layer, not a second task tracker.

## When to review
- Event-driven: accepted milestone, signed candidate, public release, material defect, change of signer/package, major shared standard or owner decision.
- On request: portfolio snapshot when returning to this chat, before choosing next development priorities, or after a lost/full conversation.
- Suggested weekly review when convenient, not an imposed cadence or configured automated job. Skip unchanged projects; do not create busywork.

## Source hierarchy
Live exact source/PR and workflow results establish implementation and test status. Owner feedback establishes the scope of physical acceptance. Exact artifact/receipt and verified storefront bytes establish distribution. APP_REGISTRY.json records signing/distribution identities and evidence; PORTFOLIO_REGISTRY.md summarizes product management state. Project handoffs describe next work. If these disagree, record the discrepancy, inspect current evidence, and never silently promote an older or draft candidate. Do not overwrite newer parallel work.

## Review procedure
1. Read central registry, current priority queue and affected product handoffs. Check live refs, exact-head CI, artifact retention and owner feedback as relevant. Mark unavailable or stale evidence.
2. Identify only meaningful changes: completed milestone, current blocker, release/upgrade risk, next coherent task, shared reuse opportunity. Separate implemented, tests passed within scope, physically accepted and publicly verified.
3. Surface urgent data loss, signing/recovery, security/privacy or released-product defects first. Keep existing installations and archives intact. Follow project security gates, especially Eden Comms.
4. Select a manageable next milestone per active project; consolidate review builds and avoid repeated CI cancellation. Do not rank by test counts or fabricate completion percentages.
5. Update affected registry rows and links using fresh file SHA; preserve other changes. Update APP_REGISTRY only against actual identity/release receipts. Update project handoffs in their own development contexts where appropriate. Record owner decisions and exact evidence, not secrets or personal saves.
6. Use templates/PORTFOLIO_REVIEW.md for a dated checkpoint when meaningful. A simple registry row update is enough for minor changes. No mandatory new report for every commit.

## Ownership and approval
Product development chats implement and test; central management chat coordinates shared changes, reviews gaps and maintains portfolio docs. Owner chooses priorities, accepts physical design and authorizes publication, paid pricing, identity/key changes, transfers, legal actions and retirement. Approval of one feature does not approve the entire build. No background monitoring or automation is implied by this process.

## Recovery
When a conversation fills or environment is lost, start with the product's latest handoff, registry and live branch/PR/CI, not an old APK link or memory alone. Verify source and identity before building. For shared work start at this repository README and the portfolio registry; use the last dated checkpoint as context, not current truth. Follow DISASTER_RECOVERY.md. Never expose key bytes or passwords, never uninstall to bypass signature mismatch.

## Next operational phase
PORT-01–07 foundational documentation complete at scoped review level. Shift to actual remediation and product development: prioritize signer recovery and durable archives, support product-specific testing and release readiness, and extract toolkit candidates only when useful and rights verified. Remaining branding, legal, privacy and commercial work is not implicitly complete. No new mandatory PORT milestone series. No app code, signing, releases or accounts modified by this process.
