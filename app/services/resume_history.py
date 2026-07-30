from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.models import ResumeAnalysis
from app.schemas.resume_schema import ResumeHistoryResponse

def get_resume_history(db: Session):

    stmt = select(ResumeAnalysis)
    result=db.execute(stmt)
    analyses = result.scalars().all()

    response = [
        ResumeHistoryResponse.model_validate(analysis)
        for analysis in analyses
    ]

    return response