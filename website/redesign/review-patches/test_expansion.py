"""Offline expansion regression; synthetic fixture never distributed."""
import copy, json, tempfile, subprocess, sys, hashlib, zipfile, shutil
from pathlib import Path
HERE=Path(__file__).resolve().parent

def run(archive):
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp); source=root/'source'
        def call(*args, ok=True):
            r=subprocess.run([sys.executable,str(HERE/'edit_site.py'),*map(str,args)],capture_output=True,text=True)
            if (r.returncode==0)!=ok: raise RuntimeError(r.stdout+r.stderr)
            return r
        call('init',archive,source)
        model=json.loads((source/'site.json').read_text())
        def save(m): (source/'site.json').write_text(json.dumps(m,ensure_ascii=False),encoding='utf-8')
        call('build',source,root/'baseline')
        with zipfile.ZipFile(archive) as z:
            original=json.loads(z.read('receipt.json'))['files']
            assert all((root/'baseline'/n).read_bytes()==z.read(n) for n in original)
        expanded=copy.deepcopy(model)
        expanded['products'].append({'route':'test-puzzle.html','group':'gridmates','card':{'css':'card','image':'<img class="tile-icon" src="assets/test-puzzle.png" alt="Synthetic test tile" width="1" height="1">','status':'Internal fixture','title':'Test Puzzle','description':'Synthetic expansion fixture only.','action':'Explore Test Puzzle'},'page':{'title':'Test Puzzle — private fixture','attrs':'','main':'<main id="main" tabindex="-1"><h1>Test Puzzle</h1><p>Internal expansion fixture only.</p><img src="assets/test-puzzle.png" alt="Synthetic test tile" width="1" height="1"><a class="action" href="gridmates.html">Return to GridMates</a></main>','tail':'\n','navigation':{'brand':'GRIDMATES','links':[['gridmates.html','Collection'],['index.html','Eden Practical']]},'credit':{'kind':'text','credit':'Internal test fixture'}}})
        # tiny valid PNG, generated solely for the synthetic test
        import struct,zlib
        def chunk(t,d): return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
        (source/'assets/test-puzzle.png').write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',1,1,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b'\x00\x22\x77\x55'))+chunk(b'IEND',b''))
        save(expanded); call('build',source,root/'expanded')
        changed=sorted(n for n in original if (root/'expanded'/n).read_bytes()!=(root/'baseline'/n).read_bytes())
        assert changed==['gridmates.html','spudacus.html'],changed
        assert 'href="test-puzzle.html"' in (root/'expanded/gridmates.html').read_text()
        assert '5 illustrated puzzle and adventure projects.' in (root/'expanded/spudacus.html').read_text()
        receipt=json.loads((root/'expanded/receipt.json').read_text())
        assert receipt['publication_authorized'] is False
        assert set(receipt['files'])==set(original)|{'test-puzzle.html','assets/test-puzzle.png'}
        assert all(hashlib.sha256((root/'expanded'/n).read_bytes()).hexdigest()==h for n,h in receipt['files'].items())
        cases={}
        for name, mutate in [('duplicate_route',lambda m:m['products'].append(copy.deepcopy(m['products'][-1]))),('unknown_group',lambda m:m['products'][-1].update(group='unknown')),('unsafe_route',lambda m:m['products'][-1].update(route='../outside.html')),('missing_asset',lambda m:m['products'][-1]['card'].update(image='<img src="assets/missing.png" alt="Missing">')),('missing_anchor',lambda m:m['products'][-1]['page']['navigation']['links'].append(['#missing','Missing'])),('publication_flag',lambda m:m.update(publication_authorized=True))]:
            bad=copy.deepcopy(expanded); mutate(bad); save(bad); dest=root/name; call('build',source,dest,ok=False); assert not dest.exists(); cases[name]='rejected'
        save(expanded); call('build',source,root/'expanded',ok=False); cases['existing_output']='rejected'
        save(model); (source/'assets/test-puzzle.png').unlink(); call('build',source,root/'restored'); assert all((root/'restored'/n).read_bytes()==(root/'baseline'/n).read_bytes() for n in original)
        return {'baseline_payloads':len(original),'expanded_pages':12,'expanded_products':7,'expanded_payloads':len(receipt['files']),'local_references':receipt['local_html_references'],'changed_existing_pages':changed,'unchanged_original_payloads':len(original)-len(changed),'negative_cases':cases,'restoration_parity':True,'publication_authorized':False}
if __name__=='__main__': print(json.dumps(run(Path(sys.argv[1])),indent=2))
