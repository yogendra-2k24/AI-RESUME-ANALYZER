from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:Yogesh123@localhost:5432/resume_analyzer"
)

engine = create_engine(DATABASE_URL)