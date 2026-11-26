import {resolve} from '../v0.2/reservations.mjs';
import {learn} from '../v0.3/learning.mjs';
import {remember,decideWithExperience} from '../v0.4/memory.mjs';
const clamp=x=>Math.max(0,Math.min(100,x));
export function simulate({population=12,ticks=100,seed=42,initialFood=12,reverseRequests=false}={}) {
  for(const [v,min,max] of [[population,1,100],[ticks,1,1000],[seed,0,4294967295],[initialFood,0,10000]]) if(!Number.isInteger(v)||v<min||v>max) throw new RangeError('Invalid scenario');
  if(typeof reverseRequests!=='boolean') throw new RangeError('Invalid request order');
  let rng=seed,food=initialFood,reservations=null;
  const random=()=>{rng=(Math.imul(rng,1664525)+1013904223)>>>0;return rng/4294967296;};
  const agents=Array.from({length:population},(_,i)=>({id:'a'+String(i).padStart(3,'0'),hunger:Math.floor(random()*50),fatigue:Math.floor(random()*50),curiosity:random(),sociability:random(),diligence:random(),memory:null,learning:null,completed:0}));
  const totals={eat:0,rest:0,gather:0,work:0,explore:0,idle:0,denied:0,criticalHungerAgentTicks:0};
  const timeline=[];
  for(let tick=0;tick<ticks;tick++) {
    const requests=[], choices=new Map();
    for(const a of agents) {
      a.hunger=clamp(a.hunger+5);a.fatigue=clamp(a.fatigue+4);
      const task=(id,kind,benefit,cost,available=true)=>({id,kind,benefit,cost,risk:0,available,skill:kind});
      const tasks=[task('meal','eat',.8,.1,food>0),task('bed-'+a.id,'rest',.7,.1),task('field','gather',.8,.3),task('workshop','work',.7,.3),task('trail','explore',.7,.2)];
      const d=decideWithExperience({...a,hunger:a.hunger/100,fatigue:a.fatigue/100,danger:0},tasks,{tick,memory:a.memory,learning:a.learning});
      const chosen=d.trace.find(t=>t.id===d.selectedId);
      choices.set(a.id,chosen);
      if(chosen.kind!=='idle') requests.push({agent:a.id,task:chosen.id,priority:chosen.priority*25+Math.max(0,Math.min(24,chosen.score/5)),duration:1});
    }
    reservations=resolve({tick,previous:reservations,requests:reverseRequests?requests.reverse():requests});
    const granted=new Set(reservations.claims.map(c=>c.agent));
    for(const a of agents) {
      const c=choices.get(a.id);
      if(!granted.has(a.id)){totals.idle++;if(c.kind!=='idle')totals.denied++;}
      else {
        if(c.kind==='eat'){if(food<=0)throw Error('Food underflow');food--;a.hunger=clamp(a.hunger-70);}
        if(c.kind==='rest')a.fatigue=clamp(a.fatigue-65);
        if(c.kind==='gather')food+=2;
        totals[c.kind]++;a.completed++;
        a.memory=remember({tick,previous:a.memory,event:{task:c.id,kind:c.kind,success:true}});
        a.learning=learn({tick,previous:a.learning,event:{skill:c.kind,kind:c.kind,effort:100,success:true}});
      }
      if(a.hunger>=85)totals.criticalHungerAgentTicks++;
    }
    timeline.push({tick,food,claims:reservations.claims.length,criticalHunger:agents.filter(a=>a.hunger>=85).length});
  }
  return {version:'population-fixture-v1',population,ticks,seed,initialFood,food,totals,timeline,agents};
}
