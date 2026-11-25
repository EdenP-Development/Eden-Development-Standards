# GridMates launcher icon standard v1.0

Owner direction 2026-11-25: the illustrated Sudoku Beta 3 launcher is the canonical visual reference, not the older vector Sudoku icon. Match green surround and margin spacing across the series. This is separate from shared startup branding.

## Verified reference
Repository EdenP-Development/SudokuTogether, commit 053fee97b88027ecd926c82e78fde7b85ab0e2dc, .github/workflows/beta3-visual-preview.yml and app/src/main/res/values/colors.xml.
- Original launcher-master.png: 1254 × 1254 PNG, SHA-256 ea3812eb46f6d3601fd5edf1d1f1f2d1c9c445a4140c7e1d2a86c08563d3367f. Stored in verified 14-part transfer archive under design/branding/transfer; archive SHA-256 487ee37d5087822e9b085b1dddf2e04b01b13a2d70d8e24dd90e60b233bf0dc8. These hashes are from the source recipe, not independent byte verification in this audit.
- Runtime background #214F3F, opaque.
- Adaptive foreground: 108dp square, rendered as 432 × 432 transparent PNG; centered 58dp artwork = 232 × 232 pixels, offset (100,100). Reference nominal 66dp central visible region = 264px, leaving 4dp/16px per side between artwork box and nominal visible boundary. Actual device mask varies.
- Preserve aspect ratio and original artwork; never overwrite master. Remove only verified exterior background as needed, preserving inner dark outlines. Optical adjustment requires screenshot evidence and owner review; nominal canvas equality does not guarantee equal gold-frame bounds.
- Reference uses Lanczos resize. Existing equivalent high-quality resampling is acceptable pending visual comparison.
- Existing preview recipe uses #123e28 in simulated mask previews, inconsistent with actual runtime #214F3F. New previews must use runtime color. Existing monochrome resource depicts old Sudoku vector; do not copy that game-specific mask to other titles.

## Shared family design
Same woodland green exterior, nominal artwork footprint and centered alignment. Consistent rounded gold frame apparent thickness, corners and negative space; retain each game's approved mascot and recognizable game motif. Exact gold contour and thickness are not yet measured from original pixels; do not claim a reusable exact frame asset exists. No new artwork needed solely to standardize padding.

## Adoption
Crossroads: existing runtime background correct, foreground currently 56dp (224px at 104,104); align to 58dp and physically compare.
Word Search and Grid Hunt: inspect active build recipe, asset bounds and adaptive resource overrides before changing; do not assume screenshot appearance establishes exact values.
Sudoku: canonical illustrated variant; preserve existing accepted appearance, fix simulated preview color separately.
Future titles: follow this recipe; pin original file hashes, maintain separate original and generated exports. For legacy launcher and Play store artwork, review separate square exports and actual target masks; exact export template pending.
Test circle, rounded-square and squircle masks, launcher and native OS splash, themed icon when supported, and small icon readability. Compare side by side on owner's phone. Preserve IDs, signing, saves and startup timing. CI plus physical visual acceptance required before publishing.

Reference master remains in Sudoku source archive; no binary duplication or independently verified exact frame template included in this revision.
