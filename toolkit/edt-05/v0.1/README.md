# EDT-05 v0.1 — Deterministic maze graph

2026-11-25. Original dependency-free JavaScript ES module; separate from existing game engines and their seed contracts. No Sector Rebound source copied or modified. Node 22.16.0 local verification; browser/WebView not yet tested.

```js
import { generateMaze } from './maze.mjs';
const map = generateMaze({width: 12, height: 9, seed: 42, braidPercent: 25, straightPercent: 50});
```

Positive integer dimensions, at most 65,536 cells, unsigned 32-bit integer seed including zero, integer percentages 0–100. Iterative depth-first traversal opens a spanning tree; straightPercent is a preference for continuing the incoming direction when available, not a guaranteed proportion. braidPercent is a chance to open each remaining internal edge, not a target loop count. Zero braid yields a tree; 100 opens all internal edges. Closed exterior, row-major array of passage bits N=1 E=2 S=4 W=8. Deterministic 32-bit LCG, non-cryptographic; do not use for security, secrets, loot fairness or adversarial multiplayer trust. Does not guarantee unique seeds, balanced arenas, gameplay difficulty or spawn fairness.

Persist version, dimensions, seed and both percentages, or exact graph bytes where appropriate. Freeze maze-v1 behavior, including traversal order and RNG draws; incompatible changes need new generator version. No existing saved seeds migrated. Rendering, walls/collision geometry, entrances/exits, multiplayer synchronization, pathfinding and fairness are separate consumer responsibilities.

```sh
node --test maze.test.mjs
```

Actual local Node 22.16.0 execution: 14/14 passed after correcting the initially guessed golden fixture to the observed generated graph (new baseline, not compatibility proof). Tests cover 100 seeds each for tree, braid and straight bias; symmetry, connectivity, boundary closure, invalid parameters, single/thin grids, maximum cell count, full braid, repeatability and frozen small fixture. Exact committed blobs match locally tested files: maze.mjs 0d79ae47c1d3db7ce706d11edb1acbb454d9c831; maze.test.mjs 1a7561e4fe4603f8c141c5193ab35729b48b05ba. No browser, Android, multiplayer or consumer tests. No CI run or product code changes. Next: pathfinding and visual preview only if a consumer needs them; verify actual product geometry and seed compatibility before adoption.
