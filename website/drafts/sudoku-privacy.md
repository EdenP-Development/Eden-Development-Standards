# GridMates: Sudoku — Beta 3 privacy notice candidate

**PREPUBLICATION DRAFT — not effective, not approved, not applicable to the existing Beta 2 release.** Do not deploy or link from an app or store. Publisher identity, monitored contact, effective date and exact delivered build must be confirmed before release.

## Playing and saving your progress
Solo and Daily puzzles are designed to work offline without a gameplay account. The Beta 3 source stores your selected display name, local installation identifier, puzzles, notes, assistance, completions, achievements, cosmetics, preferences and recent statistics on your device to continue play and show progress.

## Nearby games
Co-op and Versus use direct connections over shared Wi-Fi. Nearby discovery advertises a generic room label, room identifier, local endpoint, protocol version and room-code requirement. Connected partners exchange curated display names, appearance, gameplay information, preset Quick Chat messages and reactions; Co-op also supports temporary cell attention markers. Reconnection credentials are stored locally and exchanged with the partner. Do not share those credentials.

The host keeps up to 30 recent messages or reactions in room memory for same-partner reconnection; replacing the partner or closing the room clears that history. Cell attention markers are not saved in reconnect history. Hiding incoming communication does not delete room history. Names may remain in saved multiplayer room state. Room codes control admission, not encryption. **Nearby game traffic is not encrypted; use trusted Wi-Fi.**

## Permissions and external services
The checked source declares internet, network state, Wi-Fi state and multicast access for network sockets and discovery. It does not request contacts, camera, microphone or location permissions in the checked manifest. The source does not identify developer-operated gameplay servers or advertising, billing or analytics SDK integration. These statements require exact delivered package and dependency verification. Storefronts and services you choose to share files with may handle information under their own privacy terms.

## Backups, retention and deletion
Optional progress exports include local puzzle progress, match records, earned unlocks, achievement identifiers, selected name and preferences, excluding active rooms and reconnection credentials. Restore requires confirmation and validates imported data. The app may prune older records and retain local recovery copies. Clearing app data or uninstalling can remove local progress; export a backup first if you wish to retain it. External backup files remain under your control, and other players may hold their own copies of shared information. Account-based cloud recovery is not offered in the described source.

## Publication hold (internal)
Source: SudokuTogether feat/beta3-foundation docs/GRIDMATES_PRIVACY_POLICY_DRAFT.md blob e053a53c4e496301854e697ad94dd86d0e593fe3, checkpoint a8e1548 protocol 11. Verify exact APK, merged manifest, dependencies, network behavior, retention and restore, publisher/contact, applicable rights and request handling, audience and children's privacy, current store rules and delivered channel. Remove internal notes only after approval. No effective date or contact invented. No claim of compliance.
