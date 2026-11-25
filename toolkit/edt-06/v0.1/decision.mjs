// Original generic arcade objective selector; no engine dependency.
export const VERSION = 'arcade-objectives-v1';
const unit = (x) => typeof x === 'number' && Number.isFinite(x) && x >= 0 && x <= 1;
export function decide(state, aggression = 0.5) {
  if (!state || !unit(aggression)) throw new RangeError('Invalid state or aggression');
  for (const k of ['health','resources','threat']) if (!unit(state[k])) throw new RangeError('Invalid '+k);
  for (const k of ['canRecover','canResupply','canEvade','visibleTarget','canReposition']) if (typeof state[k] !== 'boolean') throw new RangeError('Invalid '+k);
  const {health:h,resources:r,threat:t} = state;
  const candidates = [];
  const add = (objective, eligible, score) => { if (eligible) candidates.push({objective,score}); };
  add('recover',state.canRecover && h < 0.85, (1-h)*100);
  add('resupply',state.canResupply && r < 0.85, (1-r)*85);
  add('evade',state.canEvade && t > 0, t*(1-h)*100 + t*(1-aggression)*30);
  add('engage',state.visibleTarget && r > 0 && h > 0, 20+40*aggression+20*h-25*t);
  add('reposition',state.canReposition, 15+25*t);
  add('patrol',true,10);
  const forced = h <= 0.2 && state.canRecover ? 'recover' : h <= 0.2 && t > 0 && state.canEvade ? 'evade' : null;
  let winner = candidates[0];
  for (const candidate of candidates) if (candidate.score > winner.score) winner = candidate;
  return {version:VERSION,objective:forced ?? winner.objective,reason:forced ? 'critical-health' : 'highest-score',candidates};
}
