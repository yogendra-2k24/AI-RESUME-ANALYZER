from fastapi import APIRouter, UploadFile

from app.services.resume_service import analyze_resume
from app.schemas.resume_analysis import ResumeAnalysis

# defining router with prefix and tags

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

# assigning router for resume upload

@router.post("/analyze")
def analyze_resume_endpoint(file: UploadFile) -> ResumeAnalysis:

    return analyze_resume(file)