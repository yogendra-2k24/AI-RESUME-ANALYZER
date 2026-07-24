from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.post("/upload")
def upload_resume(file: UploadFile=File(...)):
    return {
        "filename": file.filename
    }