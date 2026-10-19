"""Read-only HTTP check of public links. Saves a private review report."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
import json, subprocess
ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self): super().__init__(); self.urls=set()
 def handle_starttag(self,tag,attrs):
  if tag not in ('a','script','link','img'): return
  a=dict(attrs); u=a.get('href',a.get('src',''))
  if u.startswith('https://') and not u.startswith('https://ishandshah.github.io/portfolio/'): self.urls.add(u)
def check(url):
 p=subprocess.run(['curl','-L','-sS','--max-time','25','--output','/dev/null','--write-out','%{http_code}\t%{url_effective}',url],capture_output=True,text=True)
 parts=p.stdout.split('\t',1)
 return dict(url=url,status=parts[0],final_url=parts[-1],error=p.stderr.strip())
if __name__=='__main__':
 urls=set()
 for f in ROOT.glob('*.html'):
  p=Links();p.feed(f.read_text());urls.update(p.urls)
 with ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(check,sorted(urls)))
 out=ROOT/'tmp/portfolio-review/link-check.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(results,indent=2))
 print(json.dumps({'checked':len(results),'ok':sum(r['status'].startswith('2') for r in results),'needs_review':[r for r in results if not r['status'].startswith('2')]},indent=2))
