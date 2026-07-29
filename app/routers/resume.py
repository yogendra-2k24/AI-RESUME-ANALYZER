from fastapi import APIRouter, UploadFile, Depends

from app.services.resume_service import analyze_resume
from app.schemas.resume_analysis import ResumeAnalysis
from app.schemas.response import SuccessResponse
from app.database.database import Session, get_db

# defining router with prefix and tags

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

# assigning router for resume upload

@router.post("/analyze", response_model=SuccessResponse[ResumeAnalysis])
def analyze_resume_endpoint(file: UploadFile, db: Session = Depends(get_db)) -> ResumeAnalysis:

    result = analyze_resume(file, db)

    return SuccessResponse[ResumeAnalysis](data=result)