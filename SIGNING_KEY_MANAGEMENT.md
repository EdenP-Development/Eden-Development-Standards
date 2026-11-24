# Signing key management

## One stable identity per distribution channel
Maintain existing production and persistent QA identities. A disposable preview uses a distinct package and is never advertised as an update. Never generate a replacement key automatically when an existing key is unavailable. New apps receive their own stable identity before first distribution.

## Private custody (owner action)
1. Keep original keystore in an owner-controlled encrypted vault, outside all Git repositories. Store password in a password manager; protect vault and manager with strong authentication and recovery options.
2. Keep a second independently recoverable encrypted copy (for example encrypted offline storage). Verify recovery before first public release and periodically thereafter. Do not rely on ChatGPT sessions, runner files or expiring artifacts.
3. Record private backup location, alias, recovery instructions and verification date inside the private vault. Public registry records only package, certificate fingerprint, version, source, release evidence and non-secret custody status.
4. Configure each project's Actions secrets from the original backup using repository settings; never paste secret values into chat or logs. Secret names may vary across existing projects. GitHub secrets are build inputs, not a retrievable backup.
5. Preflight using keytool certificate SHA-256 and the pinned public fingerprint. Stop on missing/wrong secrets. Sign only trusted reviewed source in a least-privilege workflow; never run signing with untrusted PR code. Disable shell tracing, protect temporary files, clean up always, never upload keys or signing properties.
6. Verify the finished APK with apksigner and aapt. Compare package, certificate, increasing versionCode and hash; record a release receipt.

Do not consider custody established until the owner verifies both backups and an original-certificate preflight passes. A public APK contains a certificate, not the private key.
