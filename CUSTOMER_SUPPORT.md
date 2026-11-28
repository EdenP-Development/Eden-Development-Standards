# BUS-06 — Customer support and maintenance v1.0

## PORT-WEB-22 — Owner-directed lightweight support (2026-11-28)
Owner explicitly chose itch.io public comments for ordinary game feedback and deferred a dedicated support inbox, contact forms, helpdesk and paid support services. A dedicated inbox is no longer a blanket website launch gate. Public comments are not suitable for confidential or personal information; applicable private-contact, privacy, security and storefront requirements remain release-specific gates and must be resolved when required. Keep accurate visitor privacy and installation guidance. Next: final visual/content review and explicit indexing authorization; no new infrastructure. This supersedes earlier blanket contact prerequisites, not actual mandatory obligations.

Status: internal standard, 2026-11-25. No public contact, service-level agreement, refund policy, retirement date or support service is established by this document. Apply proportionately to each product, preserving stricter security and release gates.

## Support philosophy
Be approachable, honest and practical. Respect customers' time, purchases and data. Use existing tools before adding a helpdesk or account system. Do not promise 24/7 availability, guaranteed response times, indefinite updates or features not approved. Support is not an emergency service.

## Minimum setup before paid release
Establish and test one owner-controlled support contact, a private route for security/privacy reports, accessible installation/update instructions, known limitations and a short FAQ. Link the appropriate channels in the storefront and app help/about area where practical. A storefront comment thread or public GitHub issue may be useful for non-sensitive feedback but is not sufficient for confidential reports. Verify actual contact ownership and monitoring; no placeholder addresses. Maintain a single lightweight queue with product, version, issue, priority, status and next action; reuse repository issues for sanitized technical work. No additional service subscriptions required by default.

## Intake and privacy
Use templates/SUPPORT_INTAKE.md. Ask only for product/version, platform/device/OS, symptoms, reproduction steps and expected behavior. Screenshots/logs are optional and must be sanitized; never request passwords, keys, payment credentials, private communications, full personal records or unredacted backups. Use synthetic reproduction data. Keep customer contact, receipts and sensitive reports private; restrict access, establish purpose-specific retention/deletion, and honor applicable requests. Do not upload customer data to AI tools or public repositories without a reviewed lawful basis and appropriate safeguards. Do not add automatic telemetry to facilitate support.

## Triage
| Priority | Examples | Internal action |
| --- | --- | --- |
| P0 Critical | Active serious security exposure, widespread material data loss | Interrupt routine work; assess containment, affected releases and notification obligations; stop affected distribution when warranted and authorized |
| P1 High | Core workflow unavailable, serious compatibility or accessibility blocker | Prioritize investigation and safe workaround/fix; review release impact |
| P2 Normal | Noncritical bug or isolated degraded behavior | Reproduce, prioritize and schedule proportionately |
| P3 Feedback | Cosmetic issues, ideas, content requests | Acknowledge as practical, group and evaluate without promising implementation |

Severity depends on actual impact and exploitability; project-specific security classification wins. These are internal priority goals, not contractual response deadlines. Record reported vs reproduced vs verified facts. Avoid requesting destructive troubleshooting; advise backups before reset, uninstall or migration and explain possible loss.

## Security and privacy incidents
Provide a private reporting route; consider GitHub private vulnerability reporting if enabled and tested. Do not ask reporters to post exploit details, sensitive data or secrets publicly. Confirm affected versions and scope, preserve minimal protected evidence, contain, investigate and fix; coordinate responsible disclosure, review applicable breach notification deadlines and storefront requirements promptly, obtain qualified help when material. Communicate verified facts, affected versions, mitigations and uncertainty; do not claim resolution until verified. Eden Comms' charter remains binding. No automated remote kill switch or monitoring service is authorized here.

## Purchases and refunds
Identify storefront and purchase channel; use its actual refund/support process, current terms and applicable consumer rights. Verify only necessary purchase evidence privately. Distinguish defects, accidental purchases, entitlement issues and feature requests. Do not impose blanket no-refund terms or invent refund eligibility, processing times or guarantees. Owner authorizes refunds and exceptions through approved tools. No direct payment handling or new billing infrastructure by default.

## Maintenance workflow
Review queue and dependency/security/platform notices regularly at a cadence the owner can sustain; prioritize existing customer impact over speculative features. Reproduce with synthetic data, link issue to fix, run affected automated and physical QA, verify actual update/save preservation, archive exact release, write accurate release notes and obtain owner approval per RELEASE_POLICY.md. Do not silently replace published artifacts or downgrade version codes. A rollback may require a new forward-version corrective build and compatibility testing. Communicate known issues and safe workarounds; close only with evidence or explicit documented disposition.

## Support lifecycle
Use internal statuses: Active development, Maintained, Limited maintenance, Retired. Publish accurate product-specific expectations before selling; status does not cancel existing obligations. Before reducing support or retiring a product, review customer commitments, consumer law, store rules, security risks, data export and offline access. Plan reasonable notice, migration/export guidance, existing entitlement preservation where feasible, final safe release if appropriate and archival/recovery. Do not remotely disable locally functioning paid software merely because development ends. Removal from sale is distinct from revoking existing access. Owner approves actual retirement and communications; no universal lifetime or notice period set here.

## References and handoff
Follow PRIVACY_STANDARDS.md, COMMERCIAL_READINESS.md, RELEASE_POLICY.md, SAVE_PRESERVATION.md and GOOGLE_PLAY_READINESS.md. Record actual contact readiness, support status, known issues, private reporting route, maintenance capacity, unresolved incidents and next action in project handoff. Verify live storefront and legal requirements before making customer-facing promises.

## PORT-12.03 — Lightweight support operations (2026-11-26)

Extend BUS-06 and templates/SUPPORT_INTAKE.md; no new helpdesk, public contact or support commitment established. Proposed one monitored owner-controlled inbox across Spudacus/EPS, with restricted handling for confidential security/privacy reports and purchase evidence. Public storefront comments and repository issues are optional non-sensitive feedback channels, not confidential intake. Product-specific privacy notices and support expectations remain separate. Verify existing contact options privately before selecting any new address.

### Operating procedure
1. Receive a report via an approved channel; identify product, distribution channel, version, device/OS, expected and observed behavior. Ask for only necessary details; never request credentials, private communications, full backups or unredacted personal data.
2. Classify impact using existing P0–P3 severity and Reported/Investigating/Reproduced/Planned/Fixed pending verification/Verified/Closed with rationale statuses. Separate fact from allegation. Duplicate reports may link to one technical issue without copying customer identities.
3. Retain minimal confidential intake in restricted owner-controlled storage. Create sanitized technical GitHub issue only when useful; include synthetic reproduction, affected version, impact, safe workaround and acceptance criteria. No private report text, reporter email, purchase receipt or exploit details in public issues. Route security/privacy incidents privately under BUS-06 and product-specific charter.
4. Assign the next action to the relevant product lane. Reproduce against exact affected build where available; preserve installed data; avoid uninstall/clear-data advice for signature mismatch. Corrective builds follow PORT-10 exact-source, identity, upgrade and QA gates. Do not silently replace published bytes.
5. Verify the fix against the reported scenario and affected regression scope; communicate only verified resolution, remaining limitations and authorized distribution information. Close with evidence or documented disposition. Refund requests use actual storefront process and owner authorization; do not invent eligibility.
6. Review open issues at a sustainable owner-selected cadence, ahead of noncritical feature work. No automatic reminders, contractual SLA, monitoring service or telemetry added. Record retention/access/deletion rules before collecting customer records.

### Initial public help content (draft, not published)
Each product's help page should identify supported distribution channels, installation/update guidance, backup/export limitations, common troubleshooting, known issues, verified support contact and separate private security-report route. For local multiplayer, distinguish shared-Wi-Fi requirements, connection troubleshooting and actual protocol limitations. Never suggest exposing a LAN room to the internet. Use actual version-specific facts; do not imply all products have portable backups or identical connection behavior. Keep Spudacus first-person tone and EPS professional practical tone.

### Readiness and validation
- Confirm owner-approved publisher identity and dedicated contact; test a harmless inbound/outbound message from an independent account with owner authorization.
- Verify confidential reporting access and restricted storage, recovery, retention and deletion rules; test with synthetic reports only. Do not open public vulnerabilities or email real customers for a rehearsal.
- Walk through a synthetic normal bug, save-loss report and security/privacy report; verify routing, sanitized issue content, severity, safe troubleshooting and release escalation. Exercise store refund referral without initiating a refund.
- Link approved support and privacy URLs from actual product/storefront once verified; test public access and mobile readability. No placeholder links.
- Record contact test date/status, supported product scope, known-issues links and remaining gates in existing handoff/receipt. No account details or confidential evidence in public hub.

Sudoku Beta 3 remains the first publishing rehearsal candidate; public Beta 2 support should not depend on unfinished Beta 3. Word Search and Sector Rebound next-beta preparation may reuse the process. Eden Comms independent security requirements remain binding; no public functional release or sensitive-use guarantees.

This checkpoint is documentary only: no inbox, issue queue, account, customer communication, synthetic drill execution, policy publication or support service activated. Next PORT-12.04 evaluate public static site and storefront asset workflow; owner contact/host decision and actual tests remain open.
