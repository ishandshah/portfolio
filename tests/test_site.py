"""Regression checks for routes, content status, SEO, privacy, and deployment output."""
import unittest,json,re,subprocess,tempfile,hashlib,sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tags=[];self.ids=[];self.links=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if 'id' in a:self.ids.append(a['id'])
  if tag in ['a','script','link','img']:
   self.links.append(a.get('href',a.get('src','')))
class SiteTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.files={p.name:p.read_text() for p in ROOT.glob('*.html')};cls.pages={n:Page(t) for n,t in cls.files.items()}
 def test_all_original_routes_and_project_anchors(self):
  self.assertEqual(set(self.files),{'index.html','about.html','projects.html','leadership.html','speaking.html','writing.html','service.html','resume.html','contact.html'})
  for anchor in ['cloud-native-billing-platform','marketplace-inventory-platform','oracle-rms-cdc-kafka-cost-accounting','fulfillment-allocation-optimization','security-intelligence-search-platform']:
   self.assertIn(anchor,self.pages['projects.html'].ids)
 def test_unique_ids_and_landmarks(self):
  for n,p in self.pages.items():
   with self.subTest(n=n):
    self.assertEqual(len(p.ids),len(set(p.ids)))
    for tag in ['main','h1']:self.assertEqual(sum(t==tag for t,a in p.tags),1)
    self.assertTrue(any(t=='a' and a.get('href')=='#main' for t,a in p.tags))
 def test_internal_links_and_fragments(self):
  for name,p in self.pages.items():
   for url in p.links:
    u=urlsplit(url)
    if u.scheme or u.netloc:continue
    dest=(ROOT/(unquote(u.path) or name)).resolve()
    if dest.is_dir():dest=dest/'index.html'
    with self.subTest(page=name,link=url):
     self.assertTrue(dest.exists(),str(dest))
     if u.fragment and dest.suffix=='.html':self.assertIn(unquote(u.fragment),self.pages[dest.name].ids)
 def test_seo_and_jsonld(self):
  for name,text in self.files.items():
   p=self.pages[name]
   with self.subTest(page=name):
    expected='https://ishandshah.github.io/portfolio/'+('' if name=='index.html' else name)
    self.assertTrue(any(t=='link' and a.get('rel')=='canonical' and a.get('href')==expected for t,a in p.tags))
    self.assertTrue(any(t=='meta' and a.get('name')=='description' and a.get('content') for t,a in p.tags))
    for schema in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):json.loads(schema)
 def test_status_and_source_sensitive_regressions(self):
  speaking=self.files['speaking.html'];completed=speaking.split('id="completed"',1)[1].split('id="upcoming"',1)[0]
  self.assertIn('Conf42 Feature Flags 2026',completed)
  self.assertNotIn('Conf42 Platform Engineering 2026',completed)
  self.assertNotIn('Raptors Conference 2026',completed)
  self.assertIn('2026-10-22',speaking)
  self.assertIn('Co-authored with @hacker86245963',self.files['writing.html'])
  self.assertIn('NexFellow',self.files['leadership.html'])
  for s in self.files.values():
   for private in ['NL2026-','TCC-2025-','TSEC-S-','stelmakhlaw','drive.google.com/drive','/Users/','100K+ TPS','95% uptime','top 1%']:
    self.assertNotIn(private,s)
 def test_seven_complete_case_studies(self):
  s=self.files['projects.html'];self.assertEqual(s.count('class="case-study"'),7)
  for label in ['The engineering problem','The approach','Design decisions','Outcome and scope']:
   self.assertEqual(s.count(label),7)
 def test_publications_work_without_javascript(self):
  s=self.files['writing.html'];self.assertEqual(s.count('class="project-card publication"'),10)
  for p in re.findall(r'<article class="project-card publication"[^>]*>',s):self.assertNotIn(' hidden',p)
 def test_resume_alias_preserved(self):
  a=(ROOT/'assets/Ishan_Shah_Resume.pdf').read_bytes();b=(ROOT/'assets/resume/Ishan-Shah-Resume.pdf').read_bytes();self.assertEqual(a,b);self.assertTrue(a.startswith(b'%PDF'))
 def test_reproducible_safe_production_build(self):
  with tempfile.TemporaryDirectory() as t, tempfile.TemporaryDirectory() as t2:
   subprocess.run([sys.executable,str(ROOT/'scripts/build_site.py'),'--output',t],check=True,capture_output=True)
   subprocess.run([sys.executable,str(ROOT/'scripts/build_site.py'),'--output',t2],check=True,capture_output=True)
   for n in self.files:self.assertEqual((Path(t)/n).read_text(),(Path(t2)/n).read_text())
   top={p.name for p in Path(t).iterdir()};self.assertEqual(top,set(self.files)|{'assets','sitemap.xml','robots.txt','.nojekyll'})
   for p in Path(t).rglob('*'):
    self.assertNotIn('evidence',p.name.lower());self.assertNotIn('lor_',p.name.lower())
if __name__=='__main__':unittest.main()
