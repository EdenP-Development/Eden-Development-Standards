# PORT-01 — Portfolio inventory and evidence audit

Snapshot 2026-11-25. GitHub connector enumerated 7 EdenP-Development and 6 PlayerEden repositories, all default branch main and not archived. README inspected for all 12 product repositories; selected handoffs and central APP_REGISTRY.json inspected. This is an inventory/documentation audit, not an exhaustive code, branch, security, license or release verification. Do not treat repository-reported CI/publication as independently verified. Current work may be ahead of this snapshot.

## Organization projects
| Product | Repository | Evidence and stage | Priority follow-up |
| --- | --- | --- | --- |
| Sudoku | [SudokuTogether](https://github.com/EdenP-Development/SudokuTogether) | main README/handoff Nov 19 older than registry Nov 24: owner-reported public Beta 2 successor, independent download/archive and original Beta 1 key unresolved | Reconcile Beta 3 branch handoff, branding adoption and actual distribution evidence; preserve existing saves |
| Word Search | [GridMates-Word-Search](https://github.com/EdenP-Development/GridMates-Word-Search) | main README early lexicon/board work; registry QA passed, owner acceptance pending; root CONTINUE_HERE.md not found on main | Locate active branch and latest verified checkpoint; confirm private beta signing |
| Crossroads | [GridMates-Crossroads](https://github.com/EdenP-Development/GridMates-Crossroads) | main README title only; registry QA passed, owner acceptance pending; root CONTINUE_HERE.md not found on main | Locate active handoff; assess consolidated visual/physical QA and signer |
| Grid Hunt | [GridMates-Grid-Hunt](https://github.com/EdenP-Development/GridMates-Grid-Hunt) | main README GH-01 CI; docs/START_HERE.md older design-only; registry internal alpha CI passed, physical review deferred | Reconcile latest branch, alpha acceptance and backup recovery |
| Sector Rebound | [Ricochet-Rumble](https://github.com/EdenP-Development/Ricochet-Rumble) | main CONTINUE_HERE.md B1-03-D reports Android/Chromium QA pass, stacked draft PRs 155–158, owner phone review pending; private beta signer proof not actual signed beta | Reconcile active branches and owner acceptance; no bulk merge; actual beta install/update and two-phone checks |
| Eden Comms | [Eden-Comms](https://github.com/EdenP-Development/Eden-Comms) | main CONTINUE_HERE.md VIS-07, VIS-06 merged, appearance QA pending; EPS visual/startup approval not established; physical 54 cases and independent security gates open | Finish pilot within project; no production security claims |
| Infrastructure | [Eden-Development-Standards](https://github.com/EdenP-Development/Eden-Development-Standards) | central standards, APP_REGISTRY.json, BUS-01–07 | Build PORT-02 management view, not duplicate signing registry |

## PlayerEden projects
| Product | Repository | Documented baseline / next review |
| --- | --- | --- |
| The Town Was Fine | [repo](https://github.com/PlayerEden/The-Town-Was-Fine) | main README and Oct 10 PROJECT_STATE preserve v3.81 historical HTML; runtime acceptance open in docs. Check dev/active work before resuming; registry repository field currently null |
| The Last Taters | [repo](https://github.com/PlayerEden/the-last-taters) | README reports public Alpha 0.10.1, schema v16, 0.11 Settlement Maturity next. Verify actual release and current branch |
| Ant Lab (working title) | [repo](https://github.com/PlayerEden/ant-sim-sandbox) | README pre-production/research, engine not locked; prototype benchmark next |
| Operation Phosphor | [repo](https://github.com/PlayerEden/Operation-Phosphor) | README RC8 HTML and offline Android WebView Preview, emulator update check reported, physical acceptance pending |
| Potato Simulator | [repo](https://github.com/PlayerEden/potato-simulator) | README and PROJECT_STATUS v0.8.8 scene/UX closeout; mobile real-device validation next. README describes repository as private; current visibility not independently established |
| Text Adventure RPG | [repo](https://github.com/PlayerEden/text-adv-rpg) | README title only; stage unknown; inspect tree/handoff before classification |

Space Buddies has been mentioned in portfolio discussions but no matching repository was found in these two listings; do not assume it is missing, deleted or implemented. EPD storefronts are not covered by this GitHub-only inventory.

## Reuse leads (not certified components)
- The Last Taters docs/design/TATER_BRAIN_LAB.md describes rule/state/priority-driven autonomous agents, explainability and seeded comparison experiments. Adaptive weights and bandit-style methods are proposed experiments, not confirmed implementation. Inspect actual source and tests before borrowing; Sudoku coach requires constraint solving and explanation, not transplanting colony behavior.
- Sector Rebound: documented local play, profile copy/restore and deterministic visual/QA fixtures; two-phone verification remains open.
- Eden Comms handoff already references Sudoku theme roles, accessibility/visual test fixtures. Adapt presentation techniques without weakening security or using fake trust.
- Operation Phosphor: HTML-to-Android WebView packaging and emulator update rehearsal; verify source and current tooling.
- Potato Simulator: contextual UI, save slots and autonomous behavior described in project status; inspect implementations.
- Town: baseline preservation and byte-identical extraction design; verify actual dev branch before reuse.

## Immediate portfolio risks
1. Default-branch status documents can lag current development branches and central registry; do not overwrite concurrent work or confuse source merge with publication.
2. Signing custody gaps and test-only keys in central registry must remain visible. Never publish using test keys or generate replacements automatically.
3. Actual device acceptance, multi-device tests, privacy/rights inventories and commercial readiness are not established by this audit.
4. PORT-02 should record evidence date/ref, current stage, next milestone and unknowns, referencing APP_REGISTRY.json for signing/distribution. PORT-03 branding and PORT-04 standards require project-specific evidence.

No project code, branches, signing registry, repository visibility, storefront or release changed during PORT-01. No repository transfer authorized.
