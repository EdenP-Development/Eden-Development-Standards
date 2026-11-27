"""Apply hub refinement to a fresh editable source copy with V9 CSS already present."""
import json,sys
from pathlib import Path
root=Path(sys.argv[1]); path=root/'site.json'; model=json.loads(path.read_text())
h=model['hubs']; h['gridmates.html']['attrs']=' class="gridmates-hub"'; h['solutions.html']['attrs']=' class="eps eps-hub"'
old='<article class="card"><h3>GridMates</h3>'
new='<article class="card"><img src="assets/cover.webp" width="1536" height="658" alt="GridMates Sudoku illustrated cover"><h3>GridMates</h3>'
assert h['spudacus.html']['main'].count(old)==1
h['spudacus.html']['main']=h['spudacus.html']['main'].replace(old,new)
path.write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (root/'style.css').open('a') as f: f.write('\n'+Path(__file__).with_suffix('.css').read_text())
