# Original artwork pipeline

Status: adopted procedure; Crossroads transfer demonstrated, independent byte verification pending as of 2026-11-24. Do not describe an unverified candidate as release-approved.

## 1. Generate and preserve
Use approved project style references and original generated artwork. Preserve source generation IDs, original images, processing recipe, asset IDs, dimensions, alpha requirements and license/provenance. Do not regenerate approved art merely because a chat ends. Keep source libraries separate from runtime assets. Never substitute code-drawn artwork silently.

## 2. Process and package
Extract sprites, remove unwanted backgrounds, preserve proportional scale and transparent gutters, and use stable filenames. Record SHA-256 of every PNG and the final ZIP before transfer. Include a manifest and compare against the project art contract. Keep private or sensitive content out of public repositories.

## 3. Transfer through Google Drive
Reported working method from Crossroads IDENTITY-17: upload the prepared binary archive to the authorized private Drive location, retrieve its original binary bytes using the connected Drive workflow, encode bytes as base64 exactly once, create a GitHub binary blob with encoding=base64, then create a tree based on the existing branch tree, create a commit with the current branch head as parent, and update the intended development ref without force. Do not change sharing permissions. Do not use a UTF-8 text-file writer for binary content. Record archive names, original hashes, blob IDs, commit and branch in the project handoff. Exact connector invocation details from the original session are not yet independently reconstructed.

## 4. Independent verification
Checkout the committed branch in CI and compare archive SHA-256 against the pre-transfer receipt (not against a hash generated from the newly retrieved bytes). Reject mismatches, duplicate/unsafe ZIP paths, unexpected files and excessive decompressed sizes. Validate individual file hashes, PNG dimensions, alpha and transparent gutters. Use project-specific import scripts and manifest/registry validation. CI artifacts alone are not a source commit; explicitly commit validated runtime assets or use a reproducible build-time import. Retain native fallbacks and package only used artwork.

## 5. Integration and acceptance
Review visual consistency, state bounds, scaling, contrast, actual game screenshots and real-device play. Preserve app identity, saves and signing policy. Run existing regression tests and signed APK verification. Separate transfer, byte verification, runtime integration, and owner visual approval statuses.

## 6. Evidence and recovery
Crossroads reference: [IDENTITY-17 development branch](https://github.com/EdenP-Development/GridMates-Crossroads/tree/feature/identity-17-art-import), [verification workflow commit](https://github.com/EdenP-Development/GridMates-Crossroads/commit/68b6d9925a7ba5808f1f67613a79ba06f0e65a89), and docs/IDENTITY_10_ART_IMPORT.md on that branch. Both original ZIP paths were confirmed in GitHub; the workflow was committed, but its execution result has not yet been obtained. Ordinary text-file reads are not reliable binary verification. Record actual CI run and checksum results before promoting this method to independently verified. Follow the existing project handoff template when switching chats.
