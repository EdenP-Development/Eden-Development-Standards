import {decide} from '../v0.1/decision.mjs';
export const VERSION = 'simulation-memory-v1';
const need = (ok,msg) => { if (!ok) throw new RangeError(msg); };
const id = x => typeof x === 'string' && /^[A-Za-z0-9_-]{1,64}$/.test(x);
const tickOK = x => Number.isSafeInteger(x) && x >= 0;
const kinds = ['eat','rest','safety','gather','work','explore','socialize'];
const ordinary = ['gather','work','explore','socialize'];
const validEvent = e => e && id(e.task) && e.task !== 'idle' && kinds.includes(e.kind) && typeof e.success === 'boolean';
function readMemory(memory,tick) {
  if (memory === null) return [];
  need(memory.version===VERSION && tickOK(memory.tick) && memory.tick<=tick && Array.isArray(memory.events) && memory.events.length<=64,'Invalid memory');
  let last=-1;
  return memory.events.map(e=>{
    need(validEvent(e) && tickOK(e.tick) && e.tick>last && e.tick<=memory.tick,'Invalid memory event');
    last=e.tick;
    return {task:e.task,kind:e.kind,success:e.success,tick:e.tick};
  });
}
export function remember({tick,previous=null,event}) {
  need(tickOK(tick) && validEvent(event),'Invalid event or tick');
  const events=readMemory(previous,tick);
  need(previous===null || previous.tick<tick,'Tick must increase');
  events.push({task:event.task,kind:event.kind,success:event.success,tick});
  return {version:VERSION,tick,events:events.slice(-64)};
}
function readSkills(learning,tick) {
  const skills=new Map();
  if(learning===null) return skills;
  need(learning.version==='simulation-learning-v1' && tickOK(learning.tick) && learning.tick<=tick && Array.isArray(learning.skills) && learning.skills.length<=128,'Invalid learning snapshot');
  for(const s of learning.skills) {
    need(s && id(s.id) && kinds.includes(s.kind) && !skills.has(s.id) && [s.mastery,s.familiarity].every(v=>Number.isInteger(v)&&v>=0&&v<=1000),'Invalid skill');
    skills.set(s.id,s);
  }
  return skills;
}
export function decideWithExperience(agent,tasks,{tick,memory=null,learning=null,memoryTicks=100}={}) {
  need(tickOK(tick) && tickOK(memoryTicks),'Invalid clock');
  const base=decide(agent,tasks);
  const events=readMemory(memory,tick).filter(e=>tick-e.tick<=memoryTicks);
  const skills=readSkills(learning,tick);
  const byId=new Map(tasks.map(t=>[t.id,t]));
  const trace=base.trace.map(t=>{
    const task=byId.get(t.id);
    const skillId=task?.skill;
    need(skillId===undefined || id(skillId),'Invalid skill mapping');
    const skill=skills.get(skillId);
    need(!skill || skill.kind===t.kind,'Skill kind mismatch');
    const relevant=events.filter(e=>e.task===t.id && e.kind===t.kind);
    const applies=t.eligible && ordinary.includes(t.kind);
    const outcomeBonus=applies && relevant.length ? 10*relevant.reduce((n,e)=>n+(e.success?1:-1),0)/relevant.length : 0;
    const skillBonus=applies && skill ? (6*skill.mastery+4*skill.familiarity)/1000 : 0;
    return {...t,baseScore:t.score,outcomeBonus,skillBonus,score:t.score+outcomeBonus+skillBonus};
  });
  let selected=trace.find(t=>t.eligible);
  for(const t of trace) if(t.eligible && (t.priority>selected.priority || (t.priority===selected.priority && t.score>selected.score))) selected=t;
  return {version:'simulation-experience-v1',selectedId:selected.id,kind:selected.kind,reason:selected.priority>0?'survival-priority':'utility-with-experience',trace};
}
