# BUS-03 — Privacy and data handling v1.0

Status: shared engineering and commercial-readiness standard, 2026-11-25. Not a published privacy policy, legal determination, security certification or evidence of actual product behavior. Apply proportionately to each product. Stricter project requirements remain binding, including Eden Comms' Privacy and Security Charter.

## Design defaults
- Local-first where appropriate; do not require accounts, cloud storage, telemetry or advertising simply because they are available.
- Collect, retain and transmit only information required for a documented feature; choose the least intrusive workable design.
- Request minimum permissions in context, explain their purpose and handle denial/revocation without misleading the user.
- Keep saved progress and user-owned records under user control. Document export, reset, retention, backup and deletion behavior, including limitations. Do not silently delete or migrate data.
- No secret collection, sale or unrelated reuse of customer data. Remote services, analytics, ads, billing SDKs or new sensitive-data uses require explicit owner approval and a documented privacy/security review.
- Treat local multiplayer and direct device communications as networked features; offline-capable does not mean no data exchange, and local-only does not mean encrypted or anonymous.

## Inventory and evidence
Maintain a [project data inventory](templates/DATA_HANDLING_REGISTER.md) covering release-specific permissions, local storage, network endpoints and peer traffic, SDKs and dependencies, platform services, retention, backups, logs, crash reports, notifications, exports and user controls. Include data received from other users and optional features. Record collection, processing, transmission and access separately; distinguish app behavior from OS/store/keyboard behavior and unknowns.
Review actual packaged manifest, dependency tree, source paths and build variants. Verify representative runtime behavior on supported devices, with WAN available and unavailable where relevant. Test denied permissions, reset/export, backup/restore and unexpected interruption as appropriate. Network captures are scoped evidence, not proof of absence under every condition. Never capture or commit real user secrets or private communications for QA; use synthetic data and sanitize logs.

## Product-specific safeguards
- Games: preserve local profiles, progress, preferences and collections. Document LAN multiplayer discovery, player names and exchanged gameplay data. Avoid unnecessary identifiers or tracking. Evaluate age audience and children's privacy obligations before introducing network services or monetization; do not assume a child-directed or adult-only audience without review.
- EPS utilities: protect user-owned records, clarify local storage and export behavior, minimize permissions; evaluate encryption, access controls and backup according to sensitivity. No blanket promises of secure deletion, anonymity, compliance or encryption.
- Eden Comms: its [Privacy and Security Charter](https://github.com/EdenP-Development/Eden-Comms/blob/main/docs/PRIVACY_SECURITY_CHARTER.md) remains normative and stricter. This standard does not relax authentication, encryption, retention, release flags, independent review or no-ship gates. No ads or telemetry in conflict with that charter.

## Disclosures and customer controls
Prepare product-specific, plain-language privacy documentation from verified behavior, not copied boilerplate. Identify the actual responsible publisher and verified contact; explain data categories, purposes, sharing/recipients, retention, user controls, security limits, and applicable rights and request channels. Cover optional features and external links as relevant. Distinguish intended, implemented and verified behavior. Avoid absolute claims such as zero data collection, completely secure, no network traffic or irreversible deletion unless defensible and precisely scoped. Review legal requirements for actual audiences, jurisdictions, distribution and business arrangements before publication. Do not invent legal identity, contact details or compliance certifications.

## Release gates
Before public beta or update: reconcile exact build inventory, permissions, dependencies, disclosures, user controls and observed behavior. Block unexpected sensitive-data exposure, undisclosed material remote collection, misleading claims, and unresolved serious privacy/security issues. Respect stricter project gates.
Before paid distribution: repeat against exact accepted artifact; confirm support/privacy request handling, retention and third-party arrangements, rights and applicable legal review.
Before Google Play: verify current Data safety definitions, privacy policy, audience/Families, account deletion where applicable, permissions and SDK requirements directly against current official policy. Local processing and peer transfer require careful classification rather than assumptions. Ensure declarations match each distributed build and update when behavior changes.
No publication or policy submission is authorized by this document.

## Official reference starting points
- Google Play policy center: https://play.google.com/about/developer-content-policy/
- Google Play Data safety guidance: https://support.google.com/googleplay/android-developer/answer/10787469
- Android privacy and security: https://developer.android.com/privacy-and-security
- FTC business privacy resources: https://www.ftc.gov/business-guidance/privacy-security

These are research starting points, not a current legal audit. Verify applicable requirements at each release.

## Handoff
Record exact commit/build, inventory status, test evidence, known limitations, privacy policy status and unresolved items. Re-review when permissions, storage, networking, SDKs, audiences or monetization change. Keep private evidence outside public repositories.
