// Original deterministic bounded skill progression.
export const VERSION = 'simulation-learning-v1';
const id = x => typeof x === 'string' && /^[A-Za-z0-9_-]{1,64}$/.test(x);
const integer = (x,max) => Number.isSafeInteger(x) && x >= 0 && x <= max;
const need = (ok,msg) => { if (!ok) throw new RangeError(msg); };
const kinds = ['eat','rest','safety','gather','work','explore','socialize'];
export function learn({previous=null, event, tick}) {
  need(integer(tick,Number.MAX_SAFE_INTEGER),'Invalid tick');
  need(event && id(event.skill) && kinds.includes(event.kind) && integer(event.effort,100) && typeof event.success === 'boolean','Invalid event');
  const skills = new Map();
  if(previous !== null) {
    need(previous.version===VERSION && integer(previous.tick,Number.MAX_SAFE_INTEGER) && previous.tick<tick && Array.isArray(previous.skills) && previous.skills.length<=128,'Invalid previous state');
    for(const s of previous.skills) {
      need(s && id(s.id) && !skills.has(s.id) && kinds.includes(s.kind) && integer(s.mastery,1000) && integer(s.familiarity,1000),'Invalid skill');
      skills.set(s.id,{id:s.id,kind:s.kind,mastery:s.mastery,familiarity:s.familiarity});
    }
  }
  const s=skills.get(event.skill) ?? {id:event.skill,kind:event.kind,mastery:0,familiarity:0};
  need(s.kind===event.kind && (skills.has(s.id)||skills.size<128),'Skill kind mismatch or capacity');
  const gain=(value,effort,rate)=>Math.floor(effort*rate*(1000-value)/100000);
  s.mastery=Math.min(1000,s.mastery+gain(s.mastery,event.effort,event.success?20:4));
  s.familiarity=Math.min(1000,s.familiarity+gain(s.familiarity,event.effort,30));
  skills.set(s.id,s);
  return {version:VERSION,tick,skills:[...skills.values()].sort((a,b)=>a.id<b.id?-1:a.id>b.id?1:0)};
}
