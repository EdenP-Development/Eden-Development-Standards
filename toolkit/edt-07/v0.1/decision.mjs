// Original generic simulation utility selector. No world mutation or engine dependency.
export const VERSION = 'simulation-utility-v1';
const unit = v => typeof v === 'number' && Number.isFinite(v) && v >= 0 && v <= 1;
const require = (ok, message) => { if (!ok) throw new RangeError(message); };
const idOK = v => typeof v === 'string' && /^[a-zA-Z0-9_-]{1,64}$/.test(v);
const kinds = ['eat','rest','safety','gather','work','explore','socialize','idle'];
export function decide(agent, opportunities) {
  require(agent && typeof agent === 'object', 'Missing agent');
  for (const key of ['hunger','fatigue','danger','curiosity','sociability','diligence']) require(unit(agent[key]), 'Invalid '+key);
  require(Array.isArray(opportunities) && opportunities.length <= 256, 'Invalid opportunities');
  const seen = new Set();
  const trace = [];
  for (const task of opportunities) {
    require(task && idOK(task.id) && !seen.has(task.id) && task.id !== 'idle', 'Invalid or duplicate task ID');
    seen.add(task.id);
    require(kinds.includes(task.kind) && task.kind !== 'idle', 'Invalid task kind');
    require(typeof task.available === 'boolean' && unit(task.benefit) && unit(task.cost) && unit(task.risk), 'Invalid task fields');
    const drive = {eat:agent.hunger,rest:agent.fatigue,safety:agent.danger,gather:agent.diligence,work:agent.diligence,explore:agent.curiosity,socialize:agent.sociability}[task.kind];
    const priority = task.kind === 'safety' && agent.danger >= .8 ? 3 : task.kind === 'eat' && agent.hunger >= .85 ? 2 : task.kind === 'rest' && agent.fatigue >= .85 ? 1 : 0;
    const score = 70*drive + 30*task.benefit - 20*task.cost - 40*task.risk;
    trace.push({id:task.id,kind:task.kind,eligible:task.available,priority,score});
  }
  trace.push({id:'idle',kind:'idle',eligible:true,priority:0,score:0});
  trace.sort((a,b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
  let selected = trace.find(t=>t.eligible);
  for (const t of trace) if (t.eligible && (t.priority>selected.priority || (t.priority===selected.priority && t.score>selected.score))) selected=t;
  return {version:VERSION,selectedId:selected.id,kind:selected.kind,reason:selected.priority>0?'survival-priority':'utility',trace};
}
