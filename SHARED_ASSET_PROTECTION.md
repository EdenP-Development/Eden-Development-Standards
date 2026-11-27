# BIP-06 — Shared asset and licensing boundaries (2026-11-27)
Status: proposed prospective policy; not a license amendment, trademark registration, or ownership determination.

## Existing grant
Root LICENSE blob a9c4922531ac72af0e00de2e98a0327c8ee3695f is MIT, Copyright (c) 2026 PlayerEden, covering software and associated documentation. It does not expressly separate creative assets. Preserve existing grants and notices; do not assume all artwork was necessarily covered or excluded. Review exact historical scope, rights holder authority, third-party terms and reliance before prospective changes. No retroactive revocation or blanket proprietary assertion.

## Shared evidence inventory
| Asset | Existing canonical documentation | Remaining protection evidence |
| --- | --- | --- |
| Spudacus v1.0 | branding/spudacus/v1.0/README.md blob 2a07ac62a3ba27e4b4153f0c212663ec19ffdd5a; runtime SHA256 74773dbda822161f73a639f959e8bce5c6e0b333a94ebeb8ee27f620d4995d25 | Verify creator/input/terms and private master recovery; trademark review |
| GridMates v1.0 | branding/gridmates/v1.0/README.md blob fdfea86f07f0fa57c66f0e3f1e701b30cdbc397b; runtime SHA256 eef6d631cac0b9523f7e0dbebac229f9a2458d36fe2e73e111d251704d9ff292 | Same; document intended consumer uses and actual derivative rights |
| EPS v1.0 | branding/eps/v1.0/README.md blob ea9fcb587fdf3cf76724745863e168c0de9f7f1b; runtime SHA256 d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516 | Same; distinguish reconstructed SVG/PNG and human edits |
| Cozy Puzzle audio | audio/gridmates/library/v0.1/README.md blob b4f24545b25beb48f45629fa2d2a614dee7991ea | Six track entitlement records, private master recovery, effects authorship; no wider distribution while unresolved |

## Proposed future organization
- Keep intentionally shared engineering scripts and generic documentation under explicit permissive terms where authorized; preserve MIT notice.
- Separately identify future brand assets, product-specific creative materials and masters, with rights and permitted distribution scope determined before publication. A separate private source library may be appropriate; no repository or visibility change authorized.
- Consumer projects reference stable asset IDs, revisions, source fingerprints and centrally recorded rights evidence; verify exact packaged use independently. Public download availability and checksum verification are not rights clearance.
- Keep current pinned asset paths working; do not move or delete assets, rewrite history or disrupt existing build-time imports. Any future scope change requires owner approval, rights review and compatibility testing.
- Use accurate actual rights holder and brand attribution; no LLC or registered mark claim. No automatic restriction of material already licensed.

## Private evidence minimum
For each shared asset group retain original files and hashes, creation date and creator/contributor roles, generation tool and applicable terms/plan evidence where relevant, third-party inputs, transformations and human contributions, permitted uses and restrictions, and verified backup/recovery status. Store contracts, receipts, account details and private locators privately. Public records only contain sanitized status/evidence references. Reuse existing archives; no redundant copies unless recovery requires them.

Inspected documentation only: LICENSE, BRAND_IDENTITY.md, ARTWORK_PIPELINE.md, ASSET_LICENSING.md and four asset guides. No independent binary rehash, archive access, legal opinion, license change or publication. Next BIP-07 private evidence checklist and owner-controlled recovery verification.

## BIP-07 — Private evidence checklist (2026-11-27)
Use [private ownership evidence checklist](templates/PRIVATE_OWNERSHIP_EVIDENCE.md) privately. Reuse existing archives and owner-controlled recovery drill; only sanitized status belongs in the hub. Bounded Drive filename searches for GridMates-Cozy-Puzzle-Masters, GridMates-SFX and Branding Kit returned no matches; this does not establish absence or loss. Existing archive documentation remains historical evidence, actual independent recovery unverified. No files moved, uploaded or sharing changed.
