"""Prepare visitor-facing copy in a private V14-derived candidate."""
import hashlib,json,re,sys,zipfile
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
PIN='61666f4365ffd16a02d2ca5508fd5ce6b2a962c58fb829f7e83ca832aefeb0f4'
REPLACEMENTS={
 'Private offline artwork pilot · historical development artwork, not gameplay screenshots.':'Development artwork · not gameplay screenshots.',
 'Private offline artwork pilot · draft environmental sprites, not gameplay screenshots.':'Environment artwork · not gameplay screenshots.',
 'Private offline artwork pilot · historical internal test captures, not release screenshots.':'Development screenshots · features may change.',
 '<p class="notice">Private preview · no storefront or support service.</p>':'',
 '<p class="notice">Private preview · not a storefront.</p>':'',
 ' — artwork pilot</title>':'</title>',
 ' · Private artwork pilot</footer>':'</footer>',
 '<p>Website concept. No claim of incorporated status.</p>':'',
 'Support and privacy information is pending review. Do not send reports or personal information through this preview.':'Find installation guidance and information about privacy. A dedicated support contact is not available yet.',
 'Website privacy draft':'Website privacy (draft)',
 'Product support draft':'Product support',
 'Internal development · Eden Practical Solutions':'In development · Eden Practical Solutions',
 'In development. No download is offered here. Features may change. Support and privacy information is pending review.':'In development. Release availability is not announced. Features may change.',
 'No download or support service is offered here. Support and privacy information is pending review.':'Release availability is not announced.',
 'Product-specific support contacts and approved privacy policies are not yet published through this website preview. Do not send personal information here.':'Dedicated support and product privacy information are not yet available. Do not send personal information through this site.',
 'Collection previews and storefront links are pending review.':'Collections and storefront links will appear here when available.',
 'Product support — Eden Practical private draft':'Product support — Eden Practical',
 'No support contact or reporting service is activated by this preview. Contact details are pending verification and approval.':'A dedicated support contact is not available yet. For Sudoku release information, visit its itch.io project via the Sudoku page.',
 'Private draft · not an active policy or support service.':'Draft information · not an active policy or support service.'
}
class Page(HTMLParser):
 def __init__(self,data):
  super().__init__();self.ids=[];self.refs=[];self.feed(data.decode())
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k=='id':self.ids.append(v)
   if k in ('href','src') and v:self.refs.append(v)
def prepare(source,dest):
 if dest.exists():raise FileExistsError(dest)
 if hashlib.sha256(source.read_bytes()).hexdigest()!=PIN:raise ValueError('Wrong V14 archive')
 with zipfile.ZipFile(source) as z:
  receipt=json.loads(z.read('receipt.json'));files=receipt['files']
  if receipt['publication_authorized'] is not False or sorted(z.namelist())!=sorted([*files,'receipt.json']):raise ValueError('Invalid receipt')
  original={n:z.read(n) for n in files}
  if any(hashlib.sha256(v).hexdigest()!=files[n] for n,v in original.items()):raise ValueError('Hash mismatch')
 payload=dict(original);counts={}
 for n,b in original.items():
  if not n.endswith('.html'):continue
  s=b.decode();count=0
  for old,new in REPLACEMENTS.items():
   count+=s.count(old);s=s.replace(old,new)
  if 'noindex,nofollow' not in s:raise ValueError('Missing review marker')
  payload[n]=s.encode();counts[n]=count
 pages={n:Page(b) for n,b in payload.items() if n.endswith('.html')};refs=0;external=set()
 for n,p in pages.items():
  if len(set(p.ids))!=len(p.ids):raise ValueError('Duplicate ID')
  if p.refs!=Page(original[n]).refs:raise ValueError('Changed references')
  for ref in p.refs:
   u=urlsplit(ref)
   if u.scheme:external.add(ref);continue
   target=u.path or n
   if target not in payload or (u.fragment and (target not in pages or u.fragment not in pages[target].ids)):raise ValueError('Broken '+ref)
   refs+=1
 receipt['files']={n:hashlib.sha256(b).hexdigest() for n,b in payload.items()}
 receipt['publication_authorized']=False
 with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED) as z:
  for n,b in sorted(payload.items()):z.writestr(n,b)
  z.writestr('receipt.json',json.dumps(receipt,indent=2)+'\n')
 with zipfile.ZipFile(dest) as z:
  assert all(hashlib.sha256(z.read(n)).hexdigest()==h for n,h in receipt['files'].items())
 result={'archive_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'bytes':dest.stat().st_size,'pages':len(pages),'payloads':len(payload),'changed_pages':[n for n in counts if payload[n]!=original[n]],'replacements':sum(counts.values()),'local_references':refs,'external_links':sorted(external),'publication_authorized':False}
 print(json.dumps(result,indent=2))
if __name__=='__main__':prepare(Path(sys.argv[1]),Path(sys.argv[2]))
