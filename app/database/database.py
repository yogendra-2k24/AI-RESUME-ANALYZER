from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

DATABASE_URL = (
    "postgresql://postgres:Yogesh123@localhost:5432/resume_analyzer"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()

    try: 
        yield db

    finally:
        db.close()