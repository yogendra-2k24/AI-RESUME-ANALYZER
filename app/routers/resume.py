from fastapi import APIRouter, UploadFile, Depends, Query

from app.services.resume_service import analyze_resume
from app.schemas.resume_analysis import ResumeAnalysis
from app.schemas.response import SuccessResponse
from app.database.database import Session, get_db
from app.services.resume_history import get_resume_history
from app.schemas.resume_schema import ResumeHistoryResponse
from app.enums.resume import SortField, SortOrder

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

@router.get("/history", response_model=list[ResumeHistoryResponse])
def resume_history(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    sort_by: SortField = SortField.CREATED_AT,
    order: SortOrder = SortOrder.DESC,
    min_score: float | None = Query(default=None, ge=0, le=100),
    db: Session = Depends(get_db)
):

    return get_resume_history(
        db,
        limit,
        offset,
        sort_by,
        order,
        min_score
    )