from models import Saramin, Jobkorea
from datetime import datetime
from database import SessionLocal
import pandas as pd

job_db = pd.read_csv('./outputs/job_korea.csv')
saram_db = pd.read_csv('./outputs/saramin.csv')

print(job_db.head())

db = SessionLocal()

for i in range(len(job_db)):
    elem = job_db.loc[i]
    company = elem['회사명']
    title = elem['채용공고 제목']
    cruit_detail = elem['채용공고 세부 사항']
    tech_detail = elem['기술 세부 사항']
    link = elem['링크']

    q = Jobkorea(company=company, title=title, cruit_detail=cruit_detail, tech_detail=tech_detail, link=link, create_time=datetime.now())
    db.add(q)
    db.commit()

for i in range(len(saram_db)):
    elem = saram_db.loc[i]
    company = elem['회사명']
    title = elem['채용공고 제목']
    cruit_detail = elem['채용공고 세부 사항']
    tech_detail = elem['기술 세부 사항']
    href = elem['링크']

    q = Saramin(company=company, title=title, cruit_detail=cruit_detail, tech_detail=tech_detail, link=link, create_time=datetime.now())
    db.add(q)
    db.commit()
    