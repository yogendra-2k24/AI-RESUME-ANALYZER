from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.resume_service import upload_resume_service

# defining router with prefix and tags

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

# assigning router for resume upload

@router.post("/upload")
def upload_resume(file: UploadFile=File(...)):

    return upload_resume_service(file)