export const VERSION = 'simulation-reservations-v1';
const id = v => typeof v === 'string' && /^[A-Za-z0-9_-]{1,64}$/.test(v);
const tickOK = v => Number.isSafeInteger(v) && v >= 0;
const need = (ok, msg) => { if (!ok) throw new RangeError(msg); };
const cmp = (a,b) => a < b ? -1 : a > b ? 1 : 0;
export function resolve({tick, previous=null, requests=[], releases=[]}) {
  need(tickOK(tick), 'Invalid tick');
  need(Array.isArray(requests) && Array.isArray(releases) && requests.length <= 4096 && releases.length <= 4096, 'Invalid batch');
  const claims = new Map(), agents = new Set(), seenTasks = new Set(), seenAgents = new Set();
  if (previous !== null) {
    need(previous.version === VERSION && tickOK(previous.tick) && previous.tick < tick && Array.isArray(previous.claims) && previous.claims.length <= 4096, 'Invalid previous state');
    for (const c of previous.claims) {
      need(c && id(c.task) && id(c.agent) && tickOK(c.expires) && c.expires > previous.tick && !seenTasks.has(c.task) && !seenAgents.has(c.agent), 'Invalid previous claim');
      seenTasks.add(c.task); seenAgents.add(c.agent);
      if (c.expires > tick) { claims.set(c.task,{...c}); agents.add(c.agent); }
    }
  }
  const releaseKeys = new Set();
  for (const r of releases) {
    need(r && id(r.task) && id(r.agent), 'Invalid release');
    const key = r.task+':'+r.agent;
    need(!releaseKeys.has(key), 'Duplicate release'); releaseKeys.add(key);
    const c = claims.get(r.task);
    if (c?.agent === r.agent) { claims.delete(r.task); agents.delete(r.agent); }
  }
  const requestAgents = new Set();
  for (const r of requests) {
    need(r && id(r.task) && id(r.agent) && Number.isFinite(r.priority) && r.priority >= 0 && r.priority <= 100 && tickOK(r.duration) && r.duration > 0 && tickOK(tick+r.duration) && !requestAgents.has(r.agent), 'Invalid or duplicate request');
    requestAgents.add(r.agent);
  }
  const outcomes=[];
  for (const r of [...requests].sort((a,b)=>b.priority-a.priority || cmp(a.agent,b.agent))) {
    const c = claims.get(r.task);
    let status;
    if (c?.agent === r.agent) { c.expires=Math.max(c.expires,tick+r.duration); status='renewed'; }
    else if (c) status='task-busy';
    else if (agents.has(r.agent)) status='agent-busy';
    else if (claims.size >= 4096) status='capacity';
    else { claims.set(r.task,{task:r.task,agent:r.agent,expires:tick+r.duration}); agents.add(r.agent); status='granted'; }
    outcomes.push({task:r.task,agent:r.agent,status});
  }
  return {version:VERSION,tick,claims:[...claims.values()].sort((a,b)=>cmp(a.task,b.task)),outcomes};
}
