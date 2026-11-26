import {allocate} from './allocate.mjs';
import {learn} from '../v0.3/learning.mjs';
import {remember,decideWithExperience} from '../v0.4/memory.mjs';
const clamp=x=>Math.max(0,Math.min(100,x));
export function simulate({population=12,ticks=100,seed=42,initialFood=12,reverseRequests=false,mealCapacity=12}={}) {
  for(const [v,min,max] of [[population,1,100],[ticks,1,1000],[seed,0,4294967295],[initialFood,0,10000],[mealCapacity,0,100]]) if(!Number.isInteger(v)||v<min||v>max) throw new RangeError('Invalid scenario');
  if(typeof reverseRequests!=='boolean') throw new RangeError('Invalid request order');
  let rng=seed,food=initialFood;
  const random=()=>{rng=(Math.imul(rng,1664525)+1013904223)>>>0;return rng/4294967296;};
  const agents=Array.from({length:population},(_,i)=>({id:'a'+String(i).padStart(3,'0'),hunger:Math.floor(random()*50),fatigue:Math.floor(random()*50),curiosity:random(),sociability:random(),diligence:random(),memory:null,learning:null,completed:0,wait:0}));
  const totals={eat:0,rest:0,gather:0,work:0,explore:0,idle:0,denied:0,fallback:0,criticalHungerAgentTicks:0};
  const timeline=[];
  for(let tick=0;tick<ticks;tick++) {
    const requests=[], kinds=new Map(), preferred=new Map();
    const capacities=[{id:'meal',capacity:Math.min(food,mealCapacity)},{id:'field',capacity:1},{id:'workshop',capacity:1},{id:'trail',capacity:1},...agents.map(a=>({id:'bed-'+a.id,capacity:1}))];
    for(const a of agents) {
      a.hunger=clamp(a.hunger+5);a.fatigue=clamp(a.fatigue+4);
      const task=(id,kind,benefit,cost,available=true)=>({id,kind,benefit,cost,risk:0,available,skill:kind});
      const tasks=[task('meal','eat',.8,.1,food>0&&mealCapacity>0),task('bed-'+a.id,'rest',.7,.1),task('field','gather',.8,.3),task('workshop','work',.7,.3),task('trail','explore',.7,.2)];
      const d=decideWithExperience({...a,hunger:a.hunger/100,fatigue:a.fatigue/100,danger:0},tasks,{tick,memory:a.memory,learning:a.learning});
      for(const t of tasks)kinds.set(t.id,t.kind);
      preferred.set(a.id,d.selectedId);
      requests.push({id:a.id,wait:a.wait,choices:d.trace.filter(t=>t.eligible&&t.id!=='idle'&&(t.priority>0||t.score>0||(t.score===0&&t.id<'idle'))).map(t=>({id:t.id,priority:t.priority,score:t.score}))});
    }
    const result=allocate(reverseRequests?requests.reverse():requests,capacities);
    const assignments=new Map(result.assignments.map(x=>[x.agent,x]));
    for(const a of agents) {
      const x=assignments.get(a.id),kind=kinds.get(x.task);
      const denied=preferred.get(a.id)!=='idle'&&preferred.get(a.id)!==x.task;
      if(denied){totals.denied++;a.wait++;}else a.wait=0;
      if(!kind)totals.idle++;
      else {
        if(denied)totals.fallback++;
        if(kind==='eat'){if(food<=0)throw Error('Food underflow');food--;a.hunger=clamp(a.hunger-70);}
        if(kind==='rest')a.fatigue=clamp(a.fatigue-65);
        if(kind==='gather')food+=2;
        totals[kind]++;a.completed++;
        a.memory=remember({tick,previous:a.memory,event:{task:x.task,kind,success:true}});
        a.learning=learn({tick,previous:a.learning,event:{skill:kind,kind,effort:100,success:true}});
      }
      if(a.hunger>=85)totals.criticalHungerAgentTicks++;
    }
    timeline.push({tick,food,claims:result.assignments.filter(x=>x.task!==null).length,criticalHunger:agents.filter(a=>a.hunger>=85).length});
  }
  return {version:'population-capacity-fixture-v1',population,ticks,seed,initialFood,mealCapacity,food,totals,timeline,agents};
}
