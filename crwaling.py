from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

from models import Saramin, Jobkorea
from datetime import datetime
from database import SessionLocal
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.jobkorea.co.kr/')
time.sleep(2)

driver.find_element(By.ID, 'gnbGi').click()
time.sleep(2)

container = driver.find_element(By.CLASS_NAME, 'tplList').find_elements(By.CLASS_NAME, 'devloopArea')

data_list = []

for elem in container:
    company = elem.find_element(By.CLASS_NAME, 'tplCo').text
    title = elem.find_element(By.CLASS_NAME, 'titBx').find_element(By.CLASS_NAME, 'normalLog').text
    cruit_detail = elem.find_element(By.CLASS_NAME, 'titBx').find_element(By.CLASS_NAME, 'etc').text
    tech_detail = elem.find_element(By.CLASS_NAME, 'dsc').text
    link = elem.find_element(By.CLASS_NAME, 'titBx').find_element(By.CLASS_NAME, 'normalLog').get_attribute('href')

    data = {
        '회사명': company,
        '채용공고 제목': title,
        '채용공고 세부 사항': cruit_detail,
        '기술 세부 사항': tech_detail,
        '링크': link
    }

    data_list.append(data)

job_db = pd.DataFrame(data_list)

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