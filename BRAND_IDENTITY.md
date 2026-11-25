# Brand identity and product attribution standard

Status: owner-directed brand architecture, 2026-11-24. Implementation is incremental; visual assets and exact Google Play display name remain subject to approval.

## Brand registry
| Identity | Role |
| --- | --- |
| Eden Practical (EP) | Umbrella for ventures; potential future LLC, not a claim of current incorporation |
| Spudacus | Personal gamer and solo indie developer identity; games and game publishing |
| Eden Practical Solutions (EPS) | Practical software and tools, including Eden Comms and Eden Command Center |
| Eden Practical Designs (EPD) | Designs, apparel, stickers, merchandise and other creative goods |
| EdenP Development | Shared engineering organization and technical standards, not a consumer-facing publisher |
| GridMates | Game series under Spudacus; individual games retain their own titles and visual identities |

## Public-facing separation
Spudacus must feel like an individual making games, not a corporate entertainment division. Use first-person creator voice for public devlogs and community interactions. Do not prominently attach EP, EPS, EPD or EdenP Development logos or corporate taglines to games. Do not imply a team, registered company, or legal ownership arrangement that has not been established. Accurate ownership, contact and business information may appear in privacy policies, legal notices, developer notes and About sections as appropriate; never conceal required disclosures.

EPS utilities use Eden Practical Solutions directly; EPD merchandise uses Eden Practical Designs. EP remains the umbrella, not a mandatory public product label.

## Product and series hierarchy
The game title is primary. Where applicable, preserve GridMates as the recognizable series brand and the subtitle as the individual title. Spudacus is the secondary creator attribution, not a replacement for product or franchise branding. Sudoku, Word Search, Grid Hunt and Crossroads are current examples; consult the project handoff for exact approved titles. Standalone games likewise retain their individual identity.

## Implementation
- Prefer a small, unobtrusive "A game by Spudacus" or "Made by Spudacus" credit in a suitable menu, credits or About screen. About-only is acceptable where the menu is crowded.
- Optional publisher mark or startup treatment requires owner approval and must not introduce forced delays, extra taps, loading regressions or visual clutter.
- EPS apps may use "Eden Practical Solutions" or EPS attribution in their About screen and appropriate product UI.
- Do not rename products, replace existing series artwork, change package/application IDs, signing keys, save paths, network identity or distribution channels for branding purposes.
- Preserve existing approved visual styles; match typography, contrast, safe areas and scaling. Check phone layouts and accessibility. Reuse approved original assets with documented provenance per ARTWORK_PIPELINE.md. No final logo assets are approved by this document; text attribution is a valid interim implementation.
- Keep release-specific versions out of evergreen logos and publisher art. Do not copy game-specific assets into unrelated games.

## Shared startup branding (owner-approved direction)
- Standalone games: Spudacus logo and name, then product menu.
- GridMates games: Spudacus logo and name, followed by a separate shared GridMates series logo/name, then product menu.
- EPS utilities: EPS logo/name, then application. No Spudacus or GridMates branding.
- No slogans, presenter text, corporate umbrella marks or legal wording on these intros. Legal disclosures belong elsewhere.
- Final artwork and animation require owner visual acceptance before distribution. Use existing approved GridMates identity; do not invent replacement series artwork.
- Target approximately one second per stage as a design starting point, not a mandatory minimum. Run alongside normal initialization where possible; skip on tap, respect reduced motion, avoid additional forced waiting, and do not replay on resume or rotation. Provide a static fallback and proceed safely if assets fail. Silent by default until audio is explicitly approved.
- Bundle versioned assets locally; never fetch branding at runtime. Support portrait and landscape, preserve aspect ratio and safe areas. Keep native OS startup separate from in-app intros; avoid redundant screens.
- Pilot on one GridMates title and one EPS utility, then adopt on normal milestones. Verify cold/warm launches, skip, reduced motion, offline startup, orientation, navigation, startup performance and existing regression gates. Record asset hashes, approval and version in each handoff.
- Until approved assets exist, projects may prepare startup integration hooks or continue using existing credits. Do not ship placeholder artwork as final.

## Publishing
Itch.io: Spudacus, personal voice and evergreen profile; keep individual project branding. Google Play: intended shared account for Spudacus and EPS for operational convenience; proposed public display name "Spudacus // EPS", pending owner confirmation and platform acceptance. Product descriptions and in-app identity distinguish the two. Redbubble: EPD is the intended storefront identity; actual rename is not yet verified. Do not create accounts or publish changes without appropriate owner authorization.

Legal/privacy: identify the actual responsible person or entity at publication, use verified contact details and app-specific disclosures. Do not use LLC or claim trademark registration before verification. Shared business infrastructure does not justify misleading statements about independence, data handling or ownership.

## Incremental adoption and QA
1. Read this standard, current project handoff, ARTWORK_PIPELINE.md and RELEASE_CHECKLIST.md.
2. Audit existing product title, series mark, creator credits, About screen, public copy and assets.
3. Identify the smallest useful attribution change; preserve accepted UI and functionality. Record proposed placement and any conflicts.
4. Implement in a normal development branch; use approved artwork only or plain text. Test layout, navigation, startup time, relevant regression checks and signed build as appropriate.
5. Record actual screenshots, test results and owner visual approval or deferrals in the handoff. Do not describe a proposed or untested change as accepted.
6. Adopt at a suitable upcoming milestone; no forced mass rebranding or emergency release.

## Handoff prompt
Read BRAND_IDENTITY.md in EdenP-Development/Eden-Development-Standards and the current project handoff. Audit current product and series branding. Add proportionate Spudacus creator attribution for games or EPS attribution for utilities, preserving product identity, approved assets, app identity, signing and saves. Use the smallest safe change; do not add a mandatory splash or corporate EP branding to games. Verify and document actual results through the existing release process. Ask the owner only for genuine visual or publishing decisions.
