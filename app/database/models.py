from sqlalchemy import Integer, String, Float, JSON,DateTime
from datetime import datetime, UTC
defualt=lambda: datetime.now(UTC)
from sqlalchemy.orm import Mapped, mappped_column

from app.database.base import Base

class ResumeAnalysis(Base):

    __tablename__ = "resume_analysis"

    id: Mapped[int] = mappped_column(
        Integer,
        primary_key=True
    )

    filename: Mapped[str] = mappped_column(
        String(255),
        nullable = False
    )

    file_path: Mapped[str] = mappped_column(
        String(500),
        nullable = False
    )

    ats_score: Mapped[float] = mappped_column(
        Float,
        nullable = False
    )

    missing_skills: Mapped[list[str]] = mappped_column(
        JSON,
        nullable = False
    )

    suggestions: Mapped[list[str]] = mappped_column(
        JSON,
        nullable = False
    )

    created_at: Mapped[datetime] = mappped_column(
        DateTime,
        default=datetime.now
    )