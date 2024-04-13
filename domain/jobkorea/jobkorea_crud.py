# db에서 데이터를 처리할 때

from models import Jobkorea
from sqlalchemy.orm import Session


def get_jobkorea_list(db: Session):
    jk_data_list = db.query(Jobkorea)\
        .order_by(Jobkorea.create_time.desc())\
        .all()
    return jk_data_list


def get_jk_detail(db: Session, jk_data_id: int):
    detail = db.query(Jobkorea).get(jk_data_id)
    return detail