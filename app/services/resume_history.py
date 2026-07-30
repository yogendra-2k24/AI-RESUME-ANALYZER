from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.models import ResumeAnalysis

def get_resume_history(db: Session):

    stmt = select(ResumeAnalysis)
    result=db.execute(stmt)
    analyses = result.scalars().all()

    return analyses