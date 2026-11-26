# EDT-07 v0.5 — Synthetic population integration fixture

Original dependency-free ES module. simulate({population=12,ticks=100,seed=42,initialFood=12,reverseRequests=false}) runs bounded synthetic scenarios (1–100 agents, 1–1000 ticks, unsigned 32-bit seed, 0–10000 initial food). Imports unchanged v0.2 reservations, v0.3 learning, v0.4 experience adapter (which imports v0.1). LCG initializes personality/needs. Each tick increases hunger/fatigue, evaluates shared meal/field/workshop/trail and private rest tasks, resolves one-tick claims, executes granted activities and updates memory/skills. One meal consumes one food; gathering adds two; rest/meal reduce respective needs; all granted activities succeed. Denied agents idle until next tick. No death, danger dynamics, actual travel, action failures, finite gathering supply, social interactions or real economic model. The result includes full agent snapshots, totals and tick timeline. This is a deliberately constrained experiment, not a balanced simulation engine or production scheduler.

## Executed tests
Node v22.16.0, node --test v0.5/population.test.mjs from edt-07 root: 11/11 passed. Four dependency source blob hashes verified locally against committed v0.1 f4d8cedca9da2c5ef083a7cbe6b40a7eb55fb015, v0.2 4bc8e40613dbe40cc75bd00b3e2617aa0d980b20, v0.3 0b428996bdea100d02e5f5c0e3c868b66b14d270, v0.4 a67b35c75773ee9c7b25967cdb7a1afbf3c84c6f. New exact tested blobs population.mjs e524601a521660d4d76e1193b0ea056fd52b406b and population.test.mjs 88cd7e1300268abd34f905aa010cec9037502223 matched GitHub readback. Earlier suites not rerun.

## Observed scenarios (seed 42, initial food 12)
| Metric | 12 agents / 100 ticks | 100 agents / 200 ticks |
|---|---:|---:|
| Eat | 92 | 200 |
| Rest | 79 | 218 |
| Gather | 100 | 198 |
| Work | 0 | 0 |
| Explore | 100 | 200 |
| Idle / denied | 829 | 19184 |
| Final food | 120 | 208 |
| Critical hunger agent-ticks after action | 16 | 16644 |
| Final critically hungry agents | 0 | 89 |

Food inventory arithmetic holds and reversed request ordering matches full output for default scenario. However single meal task per tick bottlenecks access despite surplus food. Denied agents do not reconsider alternate tasks; no work completions in either scenario. These are behavioral blockers, not successful survival/balance outcomes. Tests establish scoped invariants, not fairness or performance guarantees. Next v0.6 compare explicit meal capacity, bounded fallback rounds and fairness/aging, against frozen v0.5 baseline; retain prior module contracts. No existing game, save or release changed.
