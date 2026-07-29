from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mappped_column

from app.database.base import Base

class ResumeAnalysis(Base):

    __tablename__ = "resume_analysis"

    id: Mapped[int] = mappped_column(
        Integer,
        primary_key=True
    )