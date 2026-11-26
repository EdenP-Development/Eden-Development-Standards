// Single-tick experimental allocation; not a persistent reservation service.
export function allocate(agents, capacities) {
  const validId=x=>typeof x==='string'&&/^[A-Za-z0-9_-]{1,64}$/.test(x);
  const need=(ok)=>{if(!ok)throw new RangeError('Invalid allocation input');};
  need(Array.isArray(agents)&&agents.length<=4096&&Array.isArray(capacities)&&capacities.length<=4096);
  const remaining=new Map(), seen=new Set();
  for(const c of capacities){need(c&&validId(c.id)&&!remaining.has(c.id)&&Number.isSafeInteger(c.capacity)&&c.capacity>=0&&c.capacity<=4096);remaining.set(c.id,c.capacity);}
  const pending=agents.map(a=>{
    need(a&&validId(a.id)&&!seen.has(a.id)&&Number.isSafeInteger(a.wait)&&a.wait>=0&&Array.isArray(a.choices)&&a.choices.length<=256);seen.add(a.id);
    const ids=new Set();
    const choices=a.choices.map(c=>{need(c&&remaining.has(c.id)&&!ids.has(c.id)&&Number.isInteger(c.priority)&&c.priority>=0&&c.priority<=3&&Number.isFinite(c.score));ids.add(c.id);return {...c};}).sort((a,b)=>b.priority-a.priority||b.score-a.score||(a.id<b.id?-1:1));
    return {id:a.id,wait:a.wait,choices,index:0};
  });
  const assignments=[];
  while(pending.length){
    for(const a of pending)while(a.index<a.choices.length&&remaining.get(a.choices[a.index].id)===0)a.index++;
    pending.sort((a,b)=>{const x=a.choices[a.index],y=b.choices[b.index];return (y?.priority??-1)-(x?.priority??-1)||b.wait-a.wait||(y?.score??0)-(x?.score??0)||(a.id<b.id?-1:1);});
    const a=pending.shift(),c=a.choices[a.index];
    if(c){remaining.set(c.id,remaining.get(c.id)-1);assignments.push({agent:a.id,task:c.id,rank:a.index});}
    else assignments.push({agent:a.id,task:null,rank:null});
  }
  return {assignments:assignments.sort((a,b)=>a.agent<b.agent?-1:1),remaining:[...remaining].sort(([a],[b])=>a<b?-1:1).map(([id,capacity])=>({id,capacity}))};
}
