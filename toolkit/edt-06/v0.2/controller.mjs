import {decide} from '../v0.1/decision.mjs';
export const VERSION = 'arcade-controller-v1';
const check = (ok, msg) => { if (!ok) throw new RangeError(msg); };
const tickOK = n => Number.isSafeInteger(n) && n >= 0;
const objectives = ['recover','resupply','evade','engage','reposition','patrol'];
const pointOK = p => p && Number.isFinite(p.x) && Number.isFinite(p.y);
export function step(state, {tick, observation=null, previous=null, aggression=0.5, switchMargin=8, memoryTicks=30} = {}) {
  check(tickOK(tick) && tickOK(memoryTicks), 'Invalid tick or memory duration');
  check(Number.isFinite(switchMargin) && switchMargin >= 0 && switchMargin <= 100, 'Invalid switch margin');
  const base = decide(state, aggression);
  if (previous !== null) {
    check(previous.version === VERSION && tickOK(previous.tick) && previous.tick < tick && objectives.includes(previous.objective), 'Invalid previous controller state');
    if (previous.memory !== null) check(pointOK(previous.memory) && tickOK(previous.memory.seenTick) && previous.memory.seenTick <= previous.tick, 'Invalid memory');
  }
  check(observation === null || (state.visibleTarget && pointOK(observation)), 'Observation requires visible target and finite coordinates');
  let memory = observation === null ? previous?.memory ?? null : {x:observation.x,y:observation.y,seenTick:tick};
  if (memory && tick-memory.seenTick > memoryTicks) memory = null;
  if (memory) memory = {x:memory.x,y:memory.y,seenTick:memory.seenTick};
  let objective = base.objective, reason = base.reason;
  const current = base.candidates.find(c => c.objective === previous?.objective);
  const best = base.candidates.find(c => c.objective === objective);
  if (reason !== 'critical-health' && current && current.objective !== objective && best.score-current.score <= switchMargin) {
    objective = current.objective; reason = 'retained-within-margin';
  }
  return {version:VERSION,tick,objective,reason,memory,candidates:base.candidates};
}
