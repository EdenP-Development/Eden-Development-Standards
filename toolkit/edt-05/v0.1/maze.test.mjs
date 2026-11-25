import test from 'node:test';
import assert from 'node:assert/strict';
import {generateMaze} from './maze.mjs';
const gen = (extra={}) => generateMaze({width:12,height:9,seed:42,...extra});
function inspect(m) {
 const {width:w,height:h,cells:c}=m; let edges=0; const seen=new Set([0]), queue=[0];
 function links(i) { return [[1,i-w,4,i>=w],[2,i+1,8,i%w<w-1],[4,i+w,1,i<w*(h-1)],[8,i-1,2,i%w>0]]; }
 for(let i=0;i<c.length;i++) { assert.ok(Number.isInteger(c[i])&&c[i]>=0&&c[i]<=15); for(const [b,j,r,valid] of links(i)) if(c[i]&b) { assert.ok(valid); assert.ok(c[j]&r); edges++; } }
 for(let k=0;k<queue.length;k++) for(const [b,j] of links(queue[k])) if((c[queue[k]]&b)&&!seen.has(j)){seen.add(j);queue.push(j);}
 assert.equal(seen.size,w*h); return edges/2;
}
test('same seed and config',()=>assert.deepEqual(gen(),gen()));
test('different seeds',()=>assert.notDeepEqual(gen().cells,gen({seed:43}).cells));
test('tree connectivity and symmetry across 100 seeds',()=>{for(let seed=0;seed<100;seed++)assert.equal(inspect(gen({seed})),107);});
test('braided connectivity across 100 seeds',()=>{for(let seed=0;seed<100;seed++)assert.ok(inspect(gen({seed,braidPercent:30}))>=107);});
test('full braid opens every internal edge',()=>assert.equal(inspect(gen({braidPercent:100})),11*9+12*8));
test('single cell',()=>assert.deepEqual(gen({width:1,height:1}).cells,[0]));
test('thin grids',()=>{assert.equal(inspect(gen({width:1,height:40})),39);assert.equal(inspect(gen({width:40,height:1})),39);});
test('zero and max seed',()=>{inspect(gen({seed:0}));inspect(gen({seed:0xffffffff}));});
test('invalid dimensions',()=>{for(const x of [0,-1,1.5,Infinity,65537])assert.throws(()=>gen({width:x}),RangeError);});
test('invalid seed',()=>{for(const x of [-1,1.5,2**32,'42',NaN])assert.throws(()=>gen({seed:x}),RangeError);});
test('invalid percentages',()=>{for(const x of [-1,101,1.5,NaN])for(const k of ['straightPercent','braidPercent'])assert.throws(()=>gen({[k]:x}),RangeError);});
test('straight bias preserves connectivity',()=>{for(let seed=0;seed<100;seed++)assert.equal(inspect(gen({seed,straightPercent:100})),107);});
test('maximum supported cell count',()=>assert.equal(inspect(gen({width:256,height:256})),65535));
test('versioned golden fixture',()=>assert.deepEqual(generateMaze({width:3,height:3,seed:42}).cells,GOLDEN));
const GOLDEN = [2,12,4,4,5,5,3,11,9];
