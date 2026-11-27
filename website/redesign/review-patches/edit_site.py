"""Initialize editable private review source, or build it to a fresh directory."""
import argparse, json, hashlib, re, zipfile, tempfile, subprocess, sys
from pathlib import Path
import catalog, navigation, build_review

HERE = Path(__file__).resolve().parent

def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def initialize(archive, dest):
    if dest.exists(): raise FileExistsError(dest)
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp)
        build_review.run(archive, root/'verified')
        subprocess.run([sys.executable,str(HERE/'modular-shell.py'),'extract',str(archive),str(root/'shell')],check=True)
        pages=json.loads((root/'shell/pages.json').read_text())
        model=catalog.normalize(pages)
        nav=navigation.normalize(pages)
        for route,row in model['hubs'].items():
            model['hubs'][route]={**nav['pages'][route], 'main':row['main']}
        for record in model['products']:
            record['page']=nav['pages'][record['route']]
        model['brands']=nav['brands']
        model['publication_authorized']=False
        dest.mkdir()
        write_json(dest/'site.json',model)
        for p in (root/'verified').rglob('*'):
            if p.is_file() and p.name!='receipt.json' and p.suffix!='.html':
                target=dest/p.relative_to(root/'verified'); target.parent.mkdir(exist_ok=True,parents=True); target.write_bytes(p.read_bytes())

def build(source, dest):
    if dest.exists(): raise FileExistsError(dest)
    model=json.loads((source/'site.json').read_text())
    if model.get('publication_authorized') is not False: raise ValueError('Private review only')
    pages=navigation.expand({'brands':model['brands'],'pages':catalog.expand(model)})
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp); write_json(root/'pages.json',pages)
        subprocess.run([sys.executable,str(HERE/'modular-shell.py'),'build',str(root),str(root/'html')],check=True)
        payload={p.name:p.read_bytes() for p in (root/'html').glob('*.html')}
        payload['style.css']=(source/'style.css').read_bytes()
        for p in (source/'assets').iterdir():
            if p.is_symlink() or not p.is_file() or not re.fullmatch(r'[a-zA-Z0-9_.-]+\.(png|webp)',p.name): raise ValueError('Unsupported asset: '+p.name)
            payload['assets/'+p.name]=p.read_bytes()
        count=build_review.validate(payload)
        receipt={'publication_authorized':False,'files':{k:hashlib.sha256(v).hexdigest() for k,v in sorted(payload.items())},'local_html_references':count}
        dest.mkdir()
        for name,data in payload.items():
            p=dest/name; p.parent.mkdir(exist_ok=True,parents=True); p.write_bytes(data)
        write_json(dest/'receipt.json',receipt)
        print(json.dumps({'pages':len(pages),'products':len(model['products']),'payloads':len(payload),'references':count}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('mode',choices=['init','build']); p.add_argument('source',type=Path); p.add_argument('destination',type=Path); a=p.parse_args(); (initialize if a.mode=='init' else build)(a.source,a.destination)
