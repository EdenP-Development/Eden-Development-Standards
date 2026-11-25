# BUS-05 — Google Play readiness v1.0

Status: preparation only, 2026-11-25. No account creation, payment, listing reservation, key transfer, pricing change or publication authorized. Recheck live Google policies at each launch; this snapshot is not legal advice or a guarantee of eligibility.

## Account and business decisions
As of the review date, Google lists a US$25 one-time registration fee, personal and organization account types, identity/contact verification and a linked payments profile. Organization accounts generally require D-U-N-S verification; personal accounts may require Android device verification. Decide account type based on actual legal identity and applicable policy, not to evade testing. One account for Spudacus and EPS remains the intended approach, subject to owner decision and platform acceptance. Proposed public name is not final. Review public contact/address exposure, especially when monetizing; arrange legitimate business contact details and tax/payment records privately before registering. Never place identity documents, payment data or credentials in GitHub.

## Development now
Preserve stable package IDs, signing certificates, increasing version codes and save compatibility. Audit each existing itch/QA/production channel in APP_REGISTRY.json before selecting a Play identity. Do not automatically rename packages or assume a beta package is the permanent Play package. Maintain current SDK/dependency support, test Android behavior changes, and prepare AAB build capability when appropriate. Keep rights and data registers current; avoid unnecessary billing, ads, permissions and SDKs. Continue existing itch and internal QA workflows.

## Signing and cross-store distribution
New Play apps use Android App Bundles and Play App Signing. Distinguish upload key from installed APK app-signing key. Decide whether existing compatible app-signing key can be supplied to Play or a new identity is needed; Google-generated signing keys cannot simply be retrieved for independent signing. Review actual Play setup and supported key import/upgrade paths before committing. Never upload disposable QA keys or rotate existing keys automatically. For same-package itch/Play continuity, verify installed signing certificate, version progression, actual cross-channel upgrade and save preservation; plan separate packages or explicit portable migration if necessary. Owner authorizes any key transfer via official process. Preserve private custody, recovery and fingerprints under SIGNING_KEY_MANAGEMENT.md.

## Policy snapshot and testing
Official documentation reviewed 2026-11-25: new personal developer accounts created after November 13, 2023 generally need a closed test with at least 12 testers continuously opted in for 14 days before applying for production access. Production access is not automatic. Recruit genuine testers, obtain feedback, document fixes and meet actual Console requirements per app. Internal QA is not a substitute. Current mobile new-app/update target is Android 16 (API 36); verify form-factor exceptions, existing-app availability requirements, annual deadlines and device compatibility at launch. Check current native library/16 KB page size, bundle, SDK and policy requirements against the actual artifact.

## Monetization and storefront
Initial preference is affordable paid download; storefront handles initial purchase without adding in-app billing solely for that purpose. Choose permanent listing pricing before first publication: Google permits paid-to-free but generally not free-to-paid for the same app. Free itch distribution does not itself establish Play listing price; verify entitlement and migration promises. Service fees vary by program, market and transaction; check eligibility, actual current rates, taxes, merchant verification and refund rules before setting prices. If later adding digital purchases or ads, review current payments rules and exceptions, applicable SDK policies, privacy, purchase restoration and testing. No default fees or revenue assumptions. Prepare truthful store copy, authentic screenshots, icon and feature graphic, support contact, countries, age audience, content rating, ads declaration, app access/reviewer instructions and any applicable permissions/Families declarations. Never misrepresent AI use, security, functionality or audience.

## Privacy and release gate
Reconcile exact AAB and generated/installed APK behavior with PRIVACY_STANDARDS.md and ASSET_LICENSING.md. Prepare accessible product-specific privacy policy, Data safety form, data deletion mechanisms where applicable and other required declarations; distinguish local processing, peer transfers and SDK behavior using current Google definitions. Verify actual publisher identity and contact. Eden Comms retains all independent security and physical acceptance gates. Run commercial and technical acceptance under COMMERCIAL_READINESS.md and RELEASE_CHECKLIST.md, Play internal/closed tests, pre-launch reports as appropriate, and owner acceptance of the installed Play build. Verify listing/download after authorized publication and retain durable receipts. Monitor policy notices, compatibility and support. Do not treat automated checks or production-access eligibility as commercial approval.

## Official sources — reviewed 2026-11-25
- Account setup and fee: https://support.google.com/googleplay/android-developer/answer/6112435
- Identity and payments profile: https://support.google.com/googleplay/android-developer/answer/13628312
- Personal-account testing: https://support.google.com/googleplay/android-developer/answer/14151465
- Target API: https://support.google.com/googleplay/android-developer/answer/11926878
- App creation/AAB: https://support.google.com/googleplay/android-developer/answer/9859152
- Play App Signing: https://support.google.com/googleplay/android-developer/answer/9842756
- Pricing: https://support.google.com/googleplay/android-developer/answer/6334373
- Service fees: https://support.google.com/googleplay/android-developer/answer/112622
- Payments: https://support.google.com/googleplay/android-developer/answer/10281818
- User data: https://support.google.com/googleplay/android-developer/answer/10144311
- Data safety: https://support.google.com/googleplay/android-developer/answer/10787469
- Policy center: https://play.google.com/about/developer-content-policy/

Use templates/GOOGLE_PLAY_RELEASE_RECEIPT.md for per-app planning and evidence. Recheck policy links and actual Console prompts before acting.
