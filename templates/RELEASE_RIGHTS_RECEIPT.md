# Release rights receipt — lightweight project template
Status: draft until evidence and owner review. Use alongside ASSET_RIGHTS_REGISTER.md and RELEASE_CHECKLIST.md; applies to free and paid releases.

Product / channel / version:
Exact source commit / artifact SHA-256:
Review date / reviewer:

## Dependencies and notices
- [ ] Resolve exact release runtime graph (Android: `./gradlew :app:dependencies --configuration releaseRuntimeClasspath`; adjust for actual variant; JVM: `./gradlew :core:dependencies --configuration runtimeClasspath`). Retain reports; distinguish BOM constraints, debug/test tools and shipped components.
- [ ] Identify each resolved component/version, direct/transitive scope, upstream license and actual artifact license/NOTICE; record evidence and exceptions. Inspect final APK/AAB or other package for bundled components, resources and notice delivery; dependency graph alone is insufficient.
- [ ] Preserve required license texts, attribution, modification notices and any source/offer obligations; verify readable delivery. Do not replace project licensing or claim blanket clearance.
- [ ] Document unresolved or conflicting rights and disposition; block new distribution where material rights remain unresolved.

## Assets and branding
- [ ] Match exact packaged assets and storefront art to rights register; include fonts, vocabulary/data, music, effects, artwork and third-party code.
- [ ] Record provider/terms at creation, permitted use, human contributions and source inputs for AI-assisted assets. Commercial-use permission does not establish copyright exclusivity.
- [ ] Verify music entitlement per track, including generation date, plan coverage, remix/extension/input rights and distribution terms. Store account receipts and identifiers privately.
- [ ] Review related-market brand conflicts, attribution and claims; no registered mark or LLC representation without basis.

## Acceptance
Evidence links (sanitized):
Unresolved items / exclusions:
Notice delivery location:
Owner decision: pending / accepted for specified release / blocked
No signing, publication, legal registration, or license change authorized by completing this template. Reuse prior evidence only when exact versions, terms and use match; keep process proportionate.
