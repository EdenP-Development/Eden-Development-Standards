# GridMates Master Player Identity Standard v1.0 — approved direction, implementation pending

2026-11-25. Scope: Sudoku pilot, Word Search, Grid Hunt, Crossroads. Owner direction: one unified local/multiplayer profile, no unrestricted nickname entry; mix-and-match approved words with a generous earnable Name Collection. Supersedes earlier custom-text nickname direction. No release authorization or legal certification.

## ID-01 — Name builder
Three slots: first, optional middle, last. Approximately ten free choices per slot (initial target 10 each); randomize and browse/select individually, preview and confirm. Two-word names remain valid. Proposed starter catalog (subject to combination review):
- First: Happy, Clever, Curious, Gentle, Lucky, Brave, Cozy, Quiet, Swift, Friendly.
- Middle: Maple, Clover, Willow, Meadow, Pebble, Sunny, Moss, River, Honey, Forest.
- Last: Fox, Owl, Rabbit, Bear, Otter, Turtle, Squirrel, Badger, Hedgehog, Potato.
10 × 10 two-word and 10 × 10 × 10 three-word combinations before exclusions. Stable word IDs independent of labels; preserve slot assignment and IDs across releases. No typed fallback, user-entered suffix, or custom room label. Names need not be unique; internal identity independent of display name.

## ID-02 — Name Collection progression
Large expandable catalog of earnable words; freely available starter selection never expires. Unlock through existing achievement, completion, Daily, Co-op, Versus and collection milestones appropriate to each game. Show locked word and clear requirement; unlocked words remain owned and freely reusable. No competitive advantage, paid requirement, random paid reward, or loss of ownership when changing name. Proposed balance tiers: early achievable rewards, intermediate goals, long-term prestige. Exact words, counts and thresholds beyond starters require catalog review and balance pass. Shared vocabulary/IDs across series, per-game earning conditions; no automatic cross-app unlock synchronization or account service implied.

## ID-03 — Safe catalog and transport
Review individual words and combinations (including unintended offensive phrases and localization); deny unsafe combinations explicitly. Encode bounded stable IDs or strictly canonical allowlisted names, validate sender, host admission, received snapshots, discovery, reconnect and error UI. Reject unknown IDs and legacy arbitrary names at multiplayer boundary; version compatibility. Never rely on hiding text field alone. A remote claim of an earned cosmetic word is not proof of achievement; do not invent remote entitlement verification. Generic nearby labels retained, provide host-visible matching identifier. No arbitrary personal text exchanged via names; review other data paths independently.

## ID-04 — Save-preserving migration
Existing free-text names require one-time selection before multiplayer on updated client. Do not display/transmit legacy arbitrary names to peers, including resumed sessions; migrate host/guest names consistently without invalidating credentials or resetting boards. Preserve profile statistics, achievements, cosmetics, progress, settings, package and signing identity. Define versioned migration, atomic persistence, backup/restore compatibility and rollback limitations before runtime changes; no destructive reset. Solo remains accessible; avoid mandatory network or account. Stable IDs and earned word ownership must survive restart and supported backup/restore.

## ID-05 — Verification and adoption
Test all starter names, allowed/disallowed combinations, unlock eligibility, persistence, migration from existing saves and backups, old-client rejection, malicious wire values, resumed rooms, accessibility and compact/tablet layouts. Audit exact distributed package, privacy disclosures, audience and platform requirements; preset names reduce arbitrary text risks but do not guarantee UGC exemption or legal compliance. Use Sudoku pilot evidence before other games adopt. Companion cosmetics and the communication standard remain complementary, not separate identities.
