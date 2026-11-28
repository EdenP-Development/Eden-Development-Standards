# Release policy

Every distributed update has a named channel, stable package and signing certificate, monotonically increasing Android versionCode, exact source SHA, APK SHA-256 and verification receipt. Preserve existing channel identities; reserve separate packages for disposable review builds.

Before distribution: review source, run relevant automated QA, verify signed APK identity, test upgrade over the actual prior distributed APK with backed-up noncritical data, review release notes and obtain owner approval. Report test failures and explicitly deferred checks. Do not describe a debug-signer rehearsal as production continuity. Keep critical data-loss/security defects release-blocking.

Archive accepted original APK bytes and receipts using versioned GitHub Releases or another durable approved distribution location. Public artifacts must contain no secrets or personal data. GitHub Actions artifacts expire and are not permanent backups. Never silently replace an accepted asset. Publication requires explicit owner approval; no automatic itch.io release.

Use [release checklist](RELEASE_CHECKLIST.md). Physical test deferrals are owner decisions recorded per release, not blanket exemptions.

## Cumulative integrated owner QA
Owner-facing game and application builds must represent the complete current product, retaining all implemented and previously approved features, artwork, soundtrack, effects, haptics, progression, settings and interactions. Targeted feature tests and isolated experiments belong in internal development and automated verification; do not substitute reduced-scope APKs for integrated owner testing. Any intentional omission requires prior owner discussion and explicit agreement. Verify the exact candidate's feature and asset inventory, source revision, package, signer and checksum before delivery. If a component is blocked, disclose the blocker rather than silently omit it. Prefer existing stable dedicated QA identities, original QA signing credentials and increasing versions for cumulative testing updates, protecting all previous saves. Do not rotate keys, uninstall or clear data as a workaround. Official publication, rights, security and production upgrade gates above remain unchanged. This applies prospectively across the portfolio; no existing application identities or credentials are changed by this policy.
