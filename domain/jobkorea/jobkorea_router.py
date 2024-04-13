from fastapi import APIRouter, Depends # Depends를 사용하면 의존성을 쉽게 구현할 수 있다. -> 의존성: db를 사용할 때 객체를 생성하고 종료하는 것
from sqlalchemy.orm import Session

from database import get_db
from domain.jobkorea import jobkorea_schema, jobkorea_crud

router = APIRouter(
    prefix="/api/data",
)


@router.get("/jobkorea", response_model=list[jobkorea_schema.Jobkorea]) # 미리 설정한 필수 항목을 체크
def jobkorea_list(db:Session=Depends(get_db)):
    _jk_list = jobkorea_crud.get_jobkorea_list(db)
    return _jk_list

@router.get("/detail/{jk_data_id}", response_model=jobkorea_schema.Jobkorea)
def question_detail(jk_data_id: int, db: Session = Depends(get_db)):
    detail = jobkorea_crud.get_jk_detail(db, jk_data_id=jk_data_id)
    return detail