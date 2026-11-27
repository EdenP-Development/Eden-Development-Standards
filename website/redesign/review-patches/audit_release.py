"""Audit a private V12 archive; never extract or publish it."""
import hashlib, json, sys, zipfile, re
from pathlib import Path
PIN='f1c2f7d0ab453119a2cc6565cf4ee1247dbe1bc811ec1aeac0be36aaeab95539'
PAGES=set('index spudacus gridmates sudoku word-search grid-hunt crossroads sector-rebound solutions eden-comms designs'.split())
def audit(path):
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PIN:
        raise ValueError('Unexpected archive fingerprint')
    with zipfile.ZipFile(path) as z:
        receipt=json.loads(z.read('receipt.json'))
        files=receipt['files']
        if receipt['publication_authorized'] is not False or sorted(z.namelist())!=sorted([*files,'receipt.json']):
            raise ValueError('Invalid private archive entry set or status')
        for name,digest in files.items():
            if not (name=='style.css' or name in {p+'.html' for p in PAGES} or re.fullmatch(r'assets/[a-z0-9_-]+\.(webp|png)',name)):
                raise ValueError('Unexpected payload path: '+name)
            if hashlib.sha256(z.read(name)).hexdigest()!=digest:
                raise ValueError('Payload mismatch: '+name)
        if len(files)!=36 or not {p+'.html' for p in PAGES}<=files.keys():
            raise ValueError('Incomplete payload')
        return {'archive_sha256':PIN,'eligible_file_types':len(files),'html':11,'css':1,'artwork':24,'excluded':['receipt.json'],'publication_authorized':False,'release_status':'BLOCKED','outstanding':['owner approval','artwork clearance','privacy and support copy','external link verification','visual and accessibility acceptance','hosted navigation verification']}
if __name__=='__main__':
    print(json.dumps(audit(Path(sys.argv[1])),indent=2))
