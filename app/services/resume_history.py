from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.models import ResumeAnalysis
from app.schemas.resume_schema import ResumeHistoryResponse
from app.enums.resume import SortField, SortOrder

def get_resume_history(db: Session, limit, offset, sort_by: SortField, order: SortOrder):

    SORT_FIELD_MAP = {
    SortField.CREATED_AT: ResumeAnalysis.created_at,
    SortField.ATS_SCORE: ResumeAnalysis.ats_score,
    }

    column = SORT_FIELD_MAP[sort_by]

    if order == SortOrder.ASC:
        order_by_clause = column.asc()
    else:
        order_by_clause = column.desc()


    stmt = (select(ResumeAnalysis).order_by(order_by_clause).limit(limit).offset(offset))
    result=db.execute(stmt)
    analyses = result.scalars().all()

    response = [
        ResumeHistoryResponse.model_validate(analysis)
        for analysis in analyses
    ]

    return response