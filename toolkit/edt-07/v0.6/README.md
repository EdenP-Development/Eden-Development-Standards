# EDT-07 v0.6 — Capacity-aware allocation (partial milestone)

Original single-tick experimental allocator. allocate(agents,capacities) accepts up to 4096 agents and capacity records; each agent has unique ASCII id, nonnegative safe integer wait, up to 256 unique choices with known task id, integer priority 0..3 and finite score. Capacity records have unique ASCII id and integer capacity 0..4096. Choices sorted by priority, score and task ID. Each iteration skips exhausted options, chooses highest remaining priority across agents, then longest wait, then score, then agent ID. Assign at most one task per agent; return sorted assignments (null if none, rank is zero-based sorted choice position) and remaining capacities. No input mutation for plain snapshots. Caller MUST filter unavailable/unsafe tasks, exclude idle and any ordinary task that loses to idle, derive meal capacity from actual inventory, validate execution, maintain waiting history and update world resources. No persistent locks, atomic distributed transactions, optimal global matching or fairness guarantee; wait preference can outweigh ordinary score differences. This is separate from v0.2 reservations; no existing contract changed.

Actual Node 22.16.0 local execution node --test allocate.test.mjs: 9/9 passed. Local Git hashes matched exact committed source 7fa341fa11636f16b5364154b30ca5f1a391b209 and tests 16af065891fc8e0f82b8947f2464e2b7b83bb604. Controlled one-tick fixture: 100 agents, meal capacity 12, alternative work capacity 30; 12 meals, 30 work, 58 unassigned, unique assignments and no capacity overrun. Not comparable to longitudinal v0.5 settlement metrics. Direct raw GitHub download unavailable in local runtime; baseline source and README reopened through connector but full dependencies not reconstructed or rerun in this checkpoint. Next integrate new allocator in separate population fixture, implement explicit wait accounting and inventory-bounded meal slots, compare identical seeded scenarios with exact v0.5 baseline. Prior suites not rerun. No consumer or game modifications.

## EDT-07 v0.6 — Population integration checkpoint
Separate capacity-aware population fixture now implemented and executed. Node 22.16.0 combined allocator/population suite 16/16 passed (9 reruns, 7 new). Exact local dependency hashes matched v0.1 decision f4d8cedca9da2c5ef083a7cbe6b40a7eb55fb015, v0.3 learning 0b428996bdea100d02e5f5c0e3c868b66b14d270, v0.4 memory a67b35c75773ee9c7b25967cdb7a1afbf3c84c6f and v0.6 allocator 7fa341fa11636f16b5364154b30ca5f1a391b209. New population.mjs 7cb3de2f59124fe7d85e8327d298f33340981123 and population.test.mjs 804a295906cbb19fcfdb909975a21ae21534c1eb matched exact committed readback. Cumulative recorded cases 252 (245 prior plus 7 new). Earlier baseline not rerun; comparison uses recorded v0.5 values and fresh v0.6 execution.

Seed 42, initial food 12, meal capacity 12 bounded by start-of-tick stock, one field/workshop/trail slot, private bed per agent. Identical initial agent RNG and needs progression to v0.5; new allocation replaces one-tick reservation fixture only. Wait increments on denied first choice (even successful fallback), resets otherwise; no per-task waiting or fairness guarantee. Eligible alternatives must beat idle under original tie rules. One action per agent; gathering adds two food, eating consumes one. No borrowing against same-tick production.

| Metric | 12 agents / 100 ticks | 100 agents / 200 ticks |
|---|---:|---:|
| Eat | 210 | 410 |
| Rest | 690 | 18990 |
| Gather | 100 | 200 |
| Work | 100 | 200 |
| Explore | 100 | 200 |
| Idle | 0 | 0 |
| First-choice denials / fallback assignments | 962 | 19562 |
| Final food | 2 | 2 |
| Critical hunger agent-ticks | 0 | 14376 |
| Final critically hungry agents | 0 | 78 |

Behavioral blockers: food production capped at two units/tick; large settlement remains severely hungry despite improved access. Excessive rest (even at zero fatigue) masks idleness, first-choice denial is not eliminated, and no fairness guarantee. Next experiment: parameterize gathering capacity and gate unnecessary rest, measure meaningful activity and unmet need, separate changes through ablations. No actual game economy, performance certification, consumer integration or product changes. Preserve frozen prior versions.
