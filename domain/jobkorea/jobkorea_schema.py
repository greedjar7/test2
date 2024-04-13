# pydantic : API의 입출력 항목을 정의하고 검증할 수 있다.
# 입출력 항목의 갯수와 타입 설정
# 입출력 항목의 필수값 체크
# 입출력 항목의 데이터 검증

import datetime

from pydantic import BaseModel

class Jobkorea(BaseModel):
    id: int
    company: str
    title: str
    cruit_detail: str
    tech_detail: str
    link: str
    create_time: datetime.datetime

    # 구버전인 경우 필요한 부분 -> 혹시 몰라서
    class Config:
        orm_mode = True

class Saramin(BaseModel):
    id: int
    company: str
    title: str
    cruit_detail: str
    tech_detail: str
    link: str
    create_time: datetime.datetime

    # 구버전인 경우 필요한 부분 -> 혹시 몰라서
    class Config:
        orm_mode = True

class Wanted(BaseModel):
    id: int
    company: str
    title: str
    cruit_detail: str
    tech_detail: str
    link: str
    create_time: datetime.datetime

    # 구버전인 경우 필요한 부분 -> 혹시 몰라서
    class Config:
        orm_mode = True