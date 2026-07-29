from app.database.base import Base
from app.database.database import engine
from app.database.models import ResumeAnalysis

Base.metadata.create_all(bind=engine)