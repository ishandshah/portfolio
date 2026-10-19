"""Build a public resume from the same reviewed portfolio data. Requires reportlab."""
from pathlib import Path
from html import escape
import importlib.util, shutil
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('content',ROOT/'site/content.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
styles={
 'name':ParagraphStyle('name',fontName='Helvetica-Bold',fontSize=23,leading=28,spaceAfter=10),
 'h':ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,leading=18,spaceBefore=12,spaceAfter=8,textColor=HexColor('#174f43'),keepWithNext=True),
 'sub':ParagraphStyle('sub',fontName='Helvetica-Bold',fontSize=10.5,leading=14,spaceBefore=8,spaceAfter=5,keepWithNext=True),
 'p':ParagraphStyle('p',fontName='Helvetica',fontSize=10,leading=14,spaceAfter=7),
 'small':ParagraphStyle('small',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=6),
}
story=[]
def clean(t):return escape(t.replace('–','-').replace('—','-').replace('’',"'").replace('“','"').replace('”','"'))
def p(t,k='p'):story.append(Paragraph(clean(t),styles[k]))
def a(url,title,k='small'):story.append(Paragraph('<a href="'+escape(url,quote=True)+'" color="#174f43">'+clean(title)+'</a>',styles[k]))
def footer(canvas,doc):
 canvas.setFont('Helvetica',8);canvas.setFillColor(HexColor('#5d6966'));canvas.drawString(48,28,'Ishan Shah | Professional resume | October 19, 2026');canvas.drawRightString(564,28,str(doc.page))
p('Ishan Shah','name');p('Senior Software Engineer | Distributed Systems | Event-Driven Platforms','sub');p('San Jose, California | ishanshah301190@gmail.com','small');a(c.BASE,'ishandshah.github.io/portfolio/')
p('Profile','h');p(c.BIO)
p('Professional Experience','h')
p('PayPal, Inc. | December 2024 - Present','sub');p('Senior Software Engineer: May 26, 2025 - Present\nPreviously MTS1 / Staff Software Engineer: December 2024 - May 25, 2025','small');p(c.CASES[0]['outcome']);p('Developed Java and Spring services for usage and subscription billing. Co-designed merchant APIs, asynchronous Kafka/MSK processing, multi-tenant controls, and recovery behavior. Contributed performance engineering, observability, runbooks, and merchant documentation.')
p('Nordstrom, Inc. | Senior Software Engineer | March 2020 - December 2024','sub');p('Design lead and platform owner for fulfillment optimization, partnering with Data Science and operational stakeholders. Led the rules-based store allocation engine and a CDC-based cost-accounting pipeline. Founding engineer on marketplace inventory infrastructure; designed partitioning changes and bounded Kafka recovery.')
p('Securonix, Inc. | Software Engineer | December 2016 - March 2020','sub');p('Developed ingestion, enrichment, and search infrastructure for security analytics. Extended Spotter query capabilities and optimized Solr routing and sharding. Contributed multi-cluster indexing, storage-tier query stitching, and SaaS historical-query paths.')
p('Education','h');p('M.S., Computer Science | California State University, Los Angeles | 2014 - 2016','small');p('B.E., Computer Engineering | Gujarat Technological University | 2008 - 2013','small')
story.append(PageBreak());p('Selected Engineering Outcomes','h')
for x in c.CASES[1:]: p(x['title'],'sub');p(x['outcome'])
p('Technical Expertise','h');p('Java, Kotlin, Python, Spring Boot, Kafka/MSK, Kafka Streams, Debezium, PostgreSQL, ClickHouse, DynamoDB, Redis, Oracle, Solr, HDFS, AWS, Kubernetes, Docker, Terraform, OpenTelemetry, Gurobi, Optimizely.','small');a(c.BASE+'projects.html','Read the detailed engineering case studies')
story.append(PageBreak());p('Publications, Speaking & Service','h')
p('Technical Publications','sub')
for x in c.PUBLICATIONS:
 a(x['url'],x['title']);p(x['publisher']+' | '+x['date']+' | '+x['byline'],'small')
p('Completed Speaking','sub');p('Conf42 Feature Flags (October 15, 2026); WeAreDevelopers North America (September 25); CloudX (September 3); KCD SF Bay Area (September 1); Zenity AI Agent Security Summit (May 27, co-presenter); AgentCon Raleigh (May 6).','small')
p('Reviewing & Professional Service','sub');p('Journal reviewer: IEEE Networking Letters, IEEE Transactions on Cloud Computing, IEEE Network, International Journal of Computers and Applications, and Journal of Cyber Security Technology. Technical book reviewer for Apress / Springer Nature; book-proposal reviewer for Manning.','small');p('Hackathon and award evaluation, technical mentoring, and startup advisory. Fellow Member, IICSPA (2026); Fellow, Hackathon Raptors (2025).','small');a(c.BASE+'service.html','Professional service');a(c.BASE+'leadership.html','Mentoring and advisory');a(c.BASE+'speaking.html#upcoming','Upcoming speaking is listed separately on the website')
file=ROOT/'assets/Ishan_Shah_Resume.pdf';SimpleDocTemplate(str(file),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=42,bottomMargin=48,title='Ishan Shah - Professional Resume',author='Ishan Shah').build(story,onFirstPage=footer,onLaterPages=footer)
shutil.copy2(file,ROOT/'assets/resume/Ishan-Shah-Resume.pdf');print(file)
