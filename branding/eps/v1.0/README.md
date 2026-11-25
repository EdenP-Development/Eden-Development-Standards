# EPS v1.0 — Eden Comms pilot
Status: owner-approved visual direction; reconstructed production candidate pending device visual acceptance and trademark review. Eden Comms only; no other application rollout.

## Artwork
Standalone vector: emblem-full-color.svg, pinned commit a28951a5c143c93d15a5d035af110513ceb918d3.
Expected SHA-256: fafcf7d6eec7a9a313a51c2b00255468483ed973b63a8aeb97f272b9f228140a.
The complete local EPS Branding Kit v1.0 contains the stacked runtime artwork, horizontal variants and favicon exports. The stacked PNG is published on main via PR #1. Use the [exact pinned runtime asset](https://github.com/EdenP-Development/Eden-Development-Standards/blob/ba9f28feac64d851b3b1df9d7dfd3a1e50416492/branding/eps/v1.0/runtime-transparent.png). Git blob 34ea8cebc26331bea90dabb803e0b6640e072030. Main readback matched the archived Drive bytes; verify the SHA-256 before bundling. Do not substitute the standalone emblem for the approved full startup lockup.
Expected runtime-transparent.png SHA-256: d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516.
Expected runtime-transparent.svg SHA-256: f4d79750da2a78e9a5b371a9175aea451d9c3baecc04b10c86ed88cc581023ff.

## Palette
Industrial amber #D6A044 (purpose); rich violet #8B42BF (ingenuity); gunmetal #626565 (reliability); clarity white #E9E8E4 (clarity); background #111214.
Brand colors are not automatically suitable for text or security indicators. Verify contrast against each surface. Preserve independent semantic success, warning, error, trust and connection roles.

## Eden Comms appearance
Audit existing Compose theme and local preference storage before editing. New installations default to EPS Signature; keep the original green palette exactly as a selectable theme (provisional label Field Green). Preserve explicit existing choices and existing light/dark behavior where applicable. Missing/invalid preferences fall back safely; migrate without resetting other settings. Settings > Appearance should apply and persist locally without activity recreation or transport changes. Keep product-specific launcher icon. No network, telemetry, permissions or dependency changes for theme selection.

## Startup
Bundle verified full EPS artwork locally. Center on #111214, preserve proportions and safe areas, silent, skip on tap, reduced motion, no additional artificial delay, no replay on rotation/resume. Native startup should not duplicate the intro. If artwork is missing, proceed safely. Theme choice does not recolor the brand mark.

## Acceptance
Separate focused PR from Beta 1 reliability work. Read Eden Comms CONTINUE_HERE.md and design/security standards. Test preference migration, persistence, switching, invalid values, accessibility contrast, large text, portrait/landscape, offline launch, lifecycle and session safety. Run exact-head CI, record actual evidence and obtain owner visual acceptance before broader EPS rollout. Do not alter package IDs, signing or release capability flags. No new APK or app integration is asserted by this guide.

## Owner-approved startup timing — 2026-11-25
Following owner feedback that startup felt too fast, Eden Comms main appearance/EpsStartup.kt (Git blob 094947254815a6b10155ba9a53b7851187353e89) now uses 250 ms linear fade-in, 2500 ms fully visible, 250 ms linear fade-out: nominal 3000 ms at normal animation scale. This supersedes the previously proposed 2.5s trial. The exact publisher artwork, #111214 background, tap/Back skip, disabled-animation bypass, ON_STOP dismissal and decode fallback remain in source. Content mounts after intro; measure initialization and accessibility impact. See [Visual Review 2 handoff](https://github.com/EdenP-Development/Eden-Comms/blob/main/CONTINUE_HERE.md) and [source](https://github.com/EdenP-Development/Eden-Comms/blob/main/app/src/main/java/com/edenpractical/comms/appearance/EpsStartup.kt). Signed internal build 10028 (source a8a48662a7244594dbde584e85044c79e1e67b9f; signing run 45574104439) was physically reviewed by the owner, who explicitly reported: “The splash was perfect and skipable.” The exact artwork, nominal three-second timing and tap skip are accepted for EPS startup. Reduced motion, orientation, lifecycle and performance still require project-specific verification. No wider EPS rollout or security approval.
