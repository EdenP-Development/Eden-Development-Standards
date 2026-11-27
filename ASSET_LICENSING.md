# BUS-02 — Intellectual property and commercial rights v1.0

Status: shared development standard, 2026-11-25. Establishes evidence and review gates, not legal clearance, trademark registration, a new software license or business formation. US-oriented baseline; verify other jurisdictions and platform terms before distribution.

## Rules for every project
Record provenance when adding artwork, icons, fonts, audio, code, dependencies, puzzle dictionaries, datasets and promotional assets. Follow ARTWORK_PIPELINE.md for original bytes, transformations and hashes. Rights verification is separate from visual approval and technical integrity. Free distribution still requires lawful rights; payment is not the first rights gate.

Use the [asset rights register template](templates/ASSET_RIGHTS_REGISTER.md). Group assets only when their source, applicable terms and use restrictions match; retain individual paths or a manifest. Record unknowns explicitly. Keep private contracts, receipts, account details and sensitive prompts outside public repositories; use sanitized evidence references.

## Rights review
- Original human-created work: record actual creator, dates, contributions and any employer, collaborator or contractual ownership restrictions. Do not assume an organization owns rights merely because it hosts the repository.
- AI-assisted work: record provider, tool/model if known, generation date, applicable plan and terms at generation, source inputs, human edits/selection/arrangement, and provenance IDs. Check commercial-use and redistribution terms, third-party rights and trademark conflicts. Permission to use an output is not proof of exclusive copyright. Under US Copyright Office guidance, human-authored expression may qualify even in AI-assisted works, but purely AI-generated expression does not qualify merely because it was prompted. Do not claim registration or exclusive ownership without a basis.
- Third-party code, libraries and engines: inventory direct and relevant transitive dependencies and versions, retain license texts/notices, check distribution and source/offer obligations, compatibility and commercial use. Copyleft is not inherently a ban on selling software; evaluate obligations against the intended distribution model. Escalate unknown or incompatible terms.
- Fonts, images, audio, words/datasets: distinguish embedding, redistribution, modification, commercial use and attribution rights. Public availability, purchase or a free download is not permission for all uses. For music check composition and recording rights separately; for dictionaries and puzzle datasets check source terms and selection/compilation rights.
- Public GitHub repositories: public visibility is not a blanket open-source license. Preserve existing licenses and third-party notices. Do not add, remove or change a project license without explicit owner approval and rights review; consider GitHub platform terms separately.

## Brand and naming
Spudacus, GridMates, Eden Practical, EPS, EPD and product names/logos are working identities, not verified registered marks. Before expanding public use or investing heavily in promotion, screen exact and similar names and designs for related goods/services. Search USPTO federal applications/registrations, state resources, internet, storefronts and relevant common-law uses; record dates, queries, findings and unresolved risks. Escalate credible conflicts for qualified trademark advice. A domain, GitHub name, store listing or LLC name does not establish clearance. No registered trademark symbol without applicable registration.

## Gates
Now: preserve source evidence, inventory existing assets incrementally, check new additions before incorporation. Unknown rights may be investigated in isolated internal work but do not assume internal use itself is authorized.
Before any public beta/update: review distributed assets and dependencies, required notices, AI disclosures and material brand conflicts; quarantine/replace unresolved material lacking a defensible rights basis. Existing releases with discovered issues require prompt triage, not automatic deletion.
Before paid release: repeat against exact release inventory; resolve outstanding commercial-use/redistribution restrictions, confirm owner/publisher authority, contributor agreements where needed, license obligations and appropriate trademark review. Document actual evidence, not blanket clearance. Obtain owner approval and legal advice when uncertainty is material.
Before Google Play: recheck actual platform terms, listing rights, developer identity, AI disclosures where applicable and territorial restrictions.

## Authoritative starting points
- US Copyright Office, copyright basics: https://www.copyright.gov/what-is-copyright/
- US Copyright Office, AI guidance and report: https://www.copyright.gov/ai/
- USPTO, comprehensive clearance: https://www.uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks
- GitHub, repository licensing: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

## Handoff
Report rights inventory status, material unknowns, evidence references, required notices and next actions. No filing, license selection, paid release or legal representation is authorized by this document. Existing security, signing and release gates remain unchanged.

## Release-specific rights receipt (BIP-04.02, 2026-11-27)
Use [release rights receipt](templates/RELEASE_RIGHTS_RECEIPT.md) with the existing asset register and release checklist. Reuse exact-version evidence where terms and use match; inspect resolved runtime dependencies and actual packaging, not just declared libraries. Preserve required notices and private entitlement evidence. No automatic license change or distribution authorization.
