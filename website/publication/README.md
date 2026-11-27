# Website publication receipt gate v0.1

Internal, offline preflight only. Copy receipt-template.json to a controlled working location for a named product, version and distribution channel. Do not fill values until supported by actual evidence. Keep confidential evidence outside public repositories. Drafts remain outside approved content paths.

Run from repository root:
    python -m unittest discover -s website/publication -v
    python website/publication/validate_publication.py path/to/receipt.json

Exit 0 means structural checks passed, not legal compliance, real identity/contact verification, actual APK verification, URL reachability or authority to deploy. Exit 1 means rejection. Approved content paths are website/approved/<product>/privacy.md and support.md; the receipt must pin exact SHA-256 of both. Do not create approved content files before review. Each review boolean is an attestation, not independently verified by the script. A separate owner-controlled release decision and exact deployment allowlist remain mandatory. No integration with deployment yet.

Known limitations: v0.1 checks selected placeholder tokens, URL syntax and selected reserved domains, not comprehensive domain validity or reachability; .example is allowed for isolated synthetic fixtures. It does not verify receipt authenticity or substantive policy accuracy. Do not treat a manually edited receipt as proof. Next harden production/fixture separation, verify content contact/URL consistency and integrate an explicit packaging gate only after host selection.

Actual local tests: exact Git blobs 114f337722a2b18da6b078fda698ebcbcdbf0cf6 (validator) and 937a9e216ff39dbdd20236ff9b93fae1cde06e5f (tests) reconstructed and independently matched with git hash-object; python -m unittest -v passed 11/11 tests. No real product receipt approved, no deployment.
