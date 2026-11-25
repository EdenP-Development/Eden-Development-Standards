// EDT-05: read-only analysis of maze-v1 passage graphs.
function require(ok, message) { if (!ok) throw new RangeError(message); }
function graph(maze) {
  require(maze && maze.version === 'maze-v1', 'Unsupported graph version');
  const {width:w,height:h,cells:c}=maze;
  require(Number.isInteger(w)&&Number.isInteger(h)&&w>0&&h>0&&w*h<=65536, 'Invalid dimensions');
  require(Array.isArray(c)&&c.length===w*h, 'Invalid cell array');
  const adj=Array.from({length:c.length},()=>[]);
  for(let i=0;i<c.length;i++) {
    require(Number.isInteger(c[i])&&c[i]>=0&&c[i]<=15,'Invalid passage bits');
    const links=[[1,i-w,4,i>=w],[2,i+1,8,i%w<w-1],[4,i+w,1,i<w*(h-1)],[8,i-1,2,i%w>0]];
    for(const [bit,j,back,valid] of links) if(c[i]&bit) {
      require(valid && (c[j]&back),'Exterior or asymmetric passage'); adj[i].push(j);
    }
  }
  return adj;
}
function bfs(adj,start) {
  const distance=new Int32Array(adj.length).fill(-1), previous=new Int32Array(adj.length).fill(-1), queue=[start];
  distance[start]=0;
  for(let k=0;k<queue.length;k++) for(const next of adj[queue[k]]) if(distance[next]===-1) {
    distance[next]=distance[queue[k]]+1; previous[next]=queue[k]; queue.push(next);
  }
  return {distance,previous,queue};
}
export function analyzeMaze(maze) {
  const adj=graph(maze), visited=bfs(adj,0).queue.length;
  require(visited===adj.length,'Disconnected graph');
  const edges=adj.reduce((sum,a)=>sum+a.length,0)/2;
  return {cells:adj.length,edges,loops:edges-adj.length+1,deadEnds:adj.filter(a=>a.length===1).length,junctions:adj.filter(a=>a.length>=3).length,connected:true};
}
export function shortestPath(maze,start,goal) {
  const adj=graph(maze);
  require([start,goal].every(i=>Number.isInteger(i)&&i>=0&&i<adj.length),'Invalid endpoint');
  const {distance,previous,queue}=bfs(adj,start);
  require(queue.length===adj.length,'Disconnected graph');
  const path=[];
  for(let i=goal;i!==-1;i=previous[i]) path.push(i);
  return path.reverse();
}
