from fastapi import APIRouter, UploadFile

from app.services.resume_service import analyze_resume
from app.schemas.resume_analysis import ResumeAnalysis
from app.schemas.response import SuccessResponse

# defining router with prefix and tags

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

# assigning router for resume upload

@router.post("/analyze", response_model=SuccessResponse[ResumeAnalysis])
def analyze_resume_endpoint(file: UploadFile) -> ResumeAnalysis:

    result = analyze_resume(file)

    return SuccessResponse[ResumeAnalysis](data=result)