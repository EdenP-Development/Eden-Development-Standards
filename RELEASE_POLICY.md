# Release policy

Every distributed update has a named channel, stable package and signing certificate, monotonically increasing Android versionCode, exact source SHA, APK SHA-256 and verification receipt. Preserve existing channel identities; reserve separate packages for disposable review builds.

Before distribution: review source, run relevant automated QA, verify signed APK identity, test upgrade over the actual prior distributed APK with backed-up noncritical data, review release notes and obtain owner approval. Report test failures and explicitly deferred checks. Do not describe a debug-signer rehearsal as production continuity. Keep critical data-loss/security defects release-blocking.

Archive accepted original APK bytes and receipts using versioned GitHub Releases or another durable approved distribution location. Public artifacts must contain no secrets or personal data. GitHub Actions artifacts expire and are not permanent backups. Never silently replace an accepted asset. Publication requires explicit owner approval; no automatic itch.io release.

Use [release checklist](RELEASE_CHECKLIST.md). Physical test deferrals are owner decisions recorded per release, not blanket exemptions.
