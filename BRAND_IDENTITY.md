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
- For games, use the owner-approved [shared game startup v1.0](branding/game-startup/v1.0/README.md): 250 ms fade-in, 1000 ms hold, 250 ms fade-out per logo at normal animation scale, #FAE7CD background. EPS startup timing is independently owner-approved: 250 ms fade-in, 2500 ms hold, 250 ms fade-out on #111214; see [EPS v1.0](branding/eps/v1.0/README.md). Run alongside normal initialization where possible; skip on tap, respect reduced motion, avoid additional forced waiting, and do not replay on resume or rotation. Provide a static fallback and proceed safely if assets fail. Silent by default until audio is explicitly approved.
- Bundle versioned assets locally; never fetch branding at runtime. Support portrait and landscape, preserve aspect ratio and safe areas. Keep native OS startup separate from in-app intros; avoid redundant screens.
- Sudoku Beta 3 Visual Review 4 is the owner-approved game startup visual pilot (source 96747991e98f78c90e10d6eda447d1be085a3674). Normal milestone adoption is authorized for other games using the [shared implementation and verification guide](branding/game-startup/v1.0/README.md), [Spudacus v1.0](branding/spudacus/v1.0/README.md) and [GridMates v1.0](branding/gridmates/v1.0/README.md). Visual and nominal timing approval does not establish physical verification of accessibility, skip, lifecycle or performance; track each game's evidence independently. No automatic publishing. EPS requires separately approved assets and validation. Verify cold/warm launches, skip, reduced motion, offline startup, orientation, navigation, startup performance and existing regression gates. Record asset hashes, approval and version in each handoff.
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
Read BRAND_IDENTITY.md in EdenP-Development/Eden-Development-Standards and the current project handoff. Audit current product and series branding. Add proportionate Spudacus creator attribution for games or EPS attribution for utilities, preserving product identity, approved assets, app identity, signing and saves. Use the smallest safe change; adopt the approved skippable game startup standard at normal milestones; do not add corporate EP branding to games. Verify and document actual results through the existing release process. Ask the owner only for genuine visual or publishing decisions.

## EPS branding and appearance pilot (owner direction, 2026-11-24)
Eden Comms is the sole initial EPS pilot. Approved visual direction: angular modular E, clarity-white framework, industrial amber #D6A044 (purpose), rich violet #8B42BF (ingenuity), gunmetal #626565 (reliability), clarity white #E9E8E4, near-black #111214. Reconstructed assets require exact-file verification and owner visual acceptance before distribution. The EPS startup mark stays consistent across interface themes. Default new-install appearance is EPS Signature; retain original green appearance as a selectable option and preserve explicit existing preferences. Theme selection is local, offline and independent of session/security state. Use semantic color tokens; preserve warning/error/trust semantics and test contrast, font scaling, persistence, cold/warm launch and reduced motion. No changes to application IDs, signing, networking or security gates. Separate visual PR from active Beta 1 reliability work; do not roll out to other EPS apps until pilot acceptance. Owner physically approved EPS startup artwork, three-second nominal timing and skip on internal Eden Comms 10028 on 2026-11-25. Other EPS app adoption remains a separate milestone, not an automatic rollout. No trademark clearance is claimed.

## Eden Practical voice and proportional design (owner direction, 2026-11-27)
EP is a personal venture with professional standards: approachable and competent, neither corporate performance nor an overly casual personal page. Use direct descriptive language and natural personality where appropriate. No mandatory umbrella slogan, forced marketing copy, lengthy introductions or manufactured humor. Use the owner's METT-TC-inspired contextual approach: assess the actual need, audience and situation before adding copy, features, branding or process. Prefer useful information and clear navigation; preserve necessary safety, accessibility, privacy, legal and release requirements. Established product-specific identities and taglines may remain where appropriate. Do not invent team size, incorporation or personal disclosures. Apply proportionately at normal milestones, not as a forced mass rebrand.

## Practical quality and modular growth (owner direction, 2026-11-27)
Build for scale, not perfection. Simple must not look cheap, unfinished or carelessly assembled. Use intentional hierarchy, spacing, readable typography, coherent artwork and purposeful controls. Preserve product personality and context; share foundations rather than forcing identical appearances. Prefer small, independently replaceable modules, stable routes and interfaces, and reusable content patterns. Add features, dependencies and infrastructure only when an actual need justifies them. Polish visible friction and maintain reliability, accessibility and security; do not pursue endless cosmetic iterations. Apply incrementally, without forced rewrites or automatic publication.
