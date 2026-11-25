# BUS-04 — Commercial release readiness v1.0

Status: shared internal quality standard, 2026-11-25. A paid release requires separate explicit owner approval. This supplements RELEASE_POLICY.md and RELEASE_CHECKLIST.md; it never overrides stricter project security, privacy, licensing or signing gates.

## Release stages
| Stage | Purpose | Distribution |
| --- | --- | --- |
| Internal preview | Investigate features and defects | Controlled QA; clearly labeled experimental |
| Public beta | Gather feedback on usable but unfinished product | Owner-approved, generally free/optional donations; disclose known limits |
| Release candidate | Freeze intended commercial scope and verify exact artifact | Controlled acceptance; no automatic publication |
| Commercial v1.0 | Deliver complete advertised value with credible support | Owner-approved paid or other selected model |

Stage names are not proof of readiness. Do not relabel a beta as commercial simply because it compiles, has polished artwork or passed CI.

## Quality gates
1. Product value: define target audience, core promise, supported devices and complete advertised workflows. Games need enjoyable, coherent play, sufficient curated content for the stated price, clear rules, fair progression and tested save/resume. EPS utilities need reliable end-to-end practical workflows, appropriate data controls and intelligible recovery. No universal content count or feature quota.
2. Usability and presentation: coherent branding, readable text, understandable onboarding, discoverable navigation, accessible controls, appropriate contrast, font scaling, reduced motion and supported orientations. Test real devices and representative users where feasible. No misleading mockups or claims.
3. Reliability: review crashes, hangs, data integrity, offline behavior, errors, interrupted workflows, multiplayer or networking where applicable, performance and resource use. Establish project-specific measurable acceptance criteria before RC; record devices, scenarios and results. Passing automated tests is not physical acceptance.
4. Distribution integrity: execute RELEASE_POLICY.md and RELEASE_CHECKLIST.md against exact reviewed source and delivered artifact; verify signatures, identity, version, checksum, actual upgrade and save preservation, durable archive and recovery. For non-Android products use equivalent platform checks.
5. Rights, privacy and security: reconcile exact shipped asset/dependency inventory against ASSET_LICENSING.md and PRIVACY_STANDARDS.md. Verify notices, publisher information, data disclosures and applicable storefront/legal requirements. Stricter product gates remain binding. Eden Comms cannot ship as a production secure messenger until its independent security and physical acceptance gates are satisfied.
6. Commercial promise: owner approves price, channel, scope, supported platforms, beta-to-paid transition, existing customer entitlements, update expectations and refund/support process. No invented commitments or mandatory new payment infrastructure. Store listing uses actual screenshots, accurate features and clear limitations.
7. Maintainability: establish a working support channel, reproducible build instructions, dependency and issue triage, recovery/rollback plan and realistic maintenance capacity. Do not promise indefinite updates, guaranteed response times or unsupported security guarantees.

## Stop conditions
Do not approve a commercial release with unresolved critical/high security defects, known material data loss, broken advertised core workflows, incompatible signing or unverified required upgrade path, material rights or privacy gaps, deceptive product claims, unavailable required support arrangements, missing applicable compliance evidence or unmet stricter project gates. Cosmetic and low-risk defects may be explicitly deferred with documented impact and owner acceptance. Never use an owner waiver to bypass law, platform requirements or mandatory security gates.

## Acceptance workflow
Define project-specific scope and criteria early; freeze candidate scope; audit exact source and package; run automated and physical tests; review actual customer experience, rights and privacy; record issues and evidence; obtain explicit owner decision; archive and verify distributed bytes; update registry/handoff. If candidate changes, rerun affected gates against the new artifact. No automatic publication, pricing changes or account actions.

Use templates/COMMERCIAL_RELEASE_RECEIPT.md alongside the existing release checklist. Status vocabulary: Not reviewed, In progress, Verified within scope, Blocked, Not applicable with rationale, Deferred low-risk with owner approval. No numerical readiness score substitutes for a mandatory gate.

## References
MONETIZATION_STRATEGY.md, ASSET_LICENSING.md, PRIVACY_STANDARDS.md, BRAND_IDENTITY.md, RELEASE_POLICY.md, RELEASE_CHECKLIST.md, ITCH_PUBLISHING_GUIDE.md. BUS-05 will cover live Google Play requirements; BUS-06 will expand support and maintenance.
