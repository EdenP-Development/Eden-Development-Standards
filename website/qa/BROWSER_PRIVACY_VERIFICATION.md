# PORT-WEB-18 — Browser privacy verification procedure
Status: shared QA procedure, 2026-11-28; not an executed audit or publication approval. Extends PRIVACY_STANDARDS.md and templates/DATA_HANDLING_REGISTER.md. Product owners retain evidence in authorized repositories.

## 1. Release identity
Record channel, listing, retrieval date, version, source ref, archive SHA-256 and unpacked file inventory/hashes. Reconcile the actual delivered package to source. If unavailable, label source-only; never substitute current development for delivered bytes. Extract in isolation; reject traversal, symlinks and unreasonable expansion. Do not execute untrusted archives outside isolated QA.

## 2. Static review
Inventory HTML, JS, CSS, workers, WASM, media, fonts, external URLs and libraries with versions/provenance. Review storage, cookies, IndexedDB, Cache API, service workers, fetch/XHR, beacons, WebSockets, WebRTC, forms, dynamic loading, redirects, permissions, device APIs, native bridges, analytics, ads and optional features. Search hits are leads, not proof; manually inspect reachable paths, minified bundles and runtime-loaded assets. Record unknowns.

## 3. Runtime matrix
Use fresh disposable Chromium contexts, synthetic game data, loopback serving of exact unpacked bytes, no personal credentials. Record browser/version, OS, viewport, origin, artifact hash and scenario. Use a pinned supported runner (Ubuntu 24.04 for current Playwright setup). Run with:
- Online-capable controlled egress: observe requests, redirects, failures, WebSocket events and worker activity; permit only reviewed destinations after explicit authorization, block/log others. Never transmit real data.
- Offline/blocked egress: record attempted external requests before blocking; keep local assets reachable; test continued play and recovery.
- Actual hosted embed: separately inspect host vs game frames/origins, storage partitioning, cookies and external requests. Use authorized clean sessions; do not bypass access controls.
Install observation before navigation, cover popups/frames/workers, and document blind spots (WebRTC, DNS, service worker interception, browser-level activity). Playwright request events are not packet capture. Use independent controlled network observation if required. No claim of zero traffic from a quiet trace.

## 4. Product scenarios
For each scenario record action, expectation, observation and pass/fail/blocked/not applicable with rationale. Capture storage key names/types/counts and changed categories, not raw player values. Compare fresh load, menu idle, play, save, reload, browser restart, preferences, optional features, deletion/reset, export/import and offline recovery where supported. Verify intended persistence and exact deletion scope including backups; distinguish site-data clearing from game controls and host-origin effects. Do not clear real player data. Test storage denial where practical. Record page errors, missing resources and failures; a blocked scenario cannot pass.

Taters Alpha 0.10.1: new garden, save/reload, slot deletion including backup, remaining profile and preferences, audio/motion settings.
Phosphor RC8: solo progress/service record, preferences, reload, same-device Dual Ops, local sync/backup metadata, absence/presence of native bridge in browser, origin data clearing. Android Preview is out of scope.
These are planned scenarios, not executed results.

## 5. Evidence and gates
Use existing DATA_HANDLING_REGISTER, attach sanitized receipt with release identity, environment, scenario outcomes, external destination origins and purpose, dependency inventory, storage categories, host/game attribution, limitations and unresolved discrepancies. Strip query strings, fragments, tokens, request bodies, cookies, raw storage values and sensitive paths from public receipts; keep restricted evidence privately. No upload of raw HAR or customer data. Verify sanitization before sharing. Unexpected material transfers, misleading disclosure or broken required controls block approval pending resolution. Mark source-reviewed, exact-artifact verified within scope, or blocked independently; no composite compliance score.

## 6. Publication
Reconcile notice with findings and actual publisher, monitored contact, audience, applicable requirements and effective date. Obtain explicit owner approval; stable HTTPS route and listing links verified afterward. Reopen affected checks on material changes. Preserve noindex and staged sitemap until authorized. This procedure does not authorize external requests, publication, app changes or storefront edits.

## Receipt minimum
Product/channel/version; artifact SHA-256 or unavailable; source ref; browser/OS/origin; scenario ID and outcome; storage categories; network origins and attribution; dependencies; limitations; reviewer/date; evidence location; notice revision; next gate.
