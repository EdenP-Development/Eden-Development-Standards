// Original EDT-05 maze-v1 implementation. No product engine dependency.
export const GENERATOR_VERSION = 'maze-v1';
export function generateMaze({width, height, seed, braidPercent = 0, straightPercent = 0}) {
  if (!Number.isInteger(width) || !Number.isInteger(height) || width < 1 || height < 1 || width * height > 65536) throw new RangeError('Invalid dimensions');
  if (!Number.isInteger(seed) || seed < 0 || seed > 0xffffffff) throw new RangeError('Expected unsigned 32-bit seed');
  for (const p of [braidPercent, straightPercent]) if (!Number.isInteger(p) || p < 0 || p > 100) throw new RangeError('Expected integer percentage 0..100');
  let state = seed >>> 0;
  const random = () => { state = (Math.imul(state, 1664525) + 1013904223) >>> 0; return state; };
  const pick = n => Math.floor(random() / 4294967296 * n);
  const count = width * height;
  const cells = Array(count).fill(0); // N=1 E=2 S=4 W=8; open passage bits.
  const seen = new Uint8Array(count);
  function neighbors(i) {
    const x=i%width, y=Math.floor(i/width), result=[];
    if(y>0) result.push([i-width,1,4]);
    if(x+1<width) result.push([i+1,2,8]);
    if(y+1<height) result.push([i+width,4,1]);
    if(x>0) result.push([i-1,8,2]);
    return result;
  }
  function open(i,[j,bit,back]) { cells[i]|=bit; cells[j]|=back; }
  const stack=[[0,0]]; seen[0]=1;
  while(stack.length) {
    const [i, direction]=stack[stack.length-1];
    const options=neighbors(i).filter(([j])=>!seen[j]);
    if(!options.length) { stack.pop(); continue; }
    const straight=options.find(([,bit])=>bit===direction);
    const next=straight && pick(100)<straightPercent ? straight : options[pick(options.length)];
    open(i,next); seen[next[0]]=1; stack.push([next[0],next[1]]);
  }
  // Each remaining undirected edge considered exactly once, in row-major order.
  for(let i=0;i<count;i++) for(const next of neighbors(i)) {
    if(next[0]>i && !(cells[i]&next[1]) && pick(100)<braidPercent) open(i,next);
  }
  return {version:GENERATOR_VERSION,width,height,seed,braidPercent,straightPercent,cells};
}
