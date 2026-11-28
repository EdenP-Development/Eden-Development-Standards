# Operation Phosphor — browser privacy notice candidate

UNAPPROVED / NOT EFFECTIVE. Scope: documented RC8 browser edition only. Source baseline 940cadeddbc94327ef97b8e1f39e5f443ee43d92, operation_phosphor_v1.6_play_games_foundation_rc8.html initial static review. Exact itch package, bridge behavior and runtime not verified. Do not deploy.

## Proposed player-facing wording (subject to verification)

Operation Phosphor stores game configuration, service record, statistics, campaign progress, credits, unlocks and lore progress in your browser's local storage. The reviewed code also includes local backup and synchronization metadata. These records help the game preserve progress.

Dual Ops is documented as same-device split-screen play. This browser notice does not describe the separate Android Preview, Google Play Games foundation or any future online multiplayer.

Browser site-data controls can remove locally stored progress for the relevant origin; doing so may permanently erase saves and other data on that origin. Storage retention depends on your browser and hosting context.

The game is distributed through itch.io, which may handle information separately under its own privacy policy: https://itch.io/docs/legal/privacy-policy. Voluntary feedback and support are separate from gameplay. Avoid posting private information publicly.

## Approval gates (not player-facing)

Confirm exact delivered archive hash and build, full dependency inventory, browser-native bridge availability and behavior, network behavior during load/play/save/reload and local play, storage origin and deletion controls, account/analytics/advertising status, audience, applicable obligations, publisher identity, monitored contact and effective date. Proposed stable route /privacy/operation-phosphor/ is not live. No policy approval or compliance finding.
