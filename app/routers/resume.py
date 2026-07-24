from fastapi import APIRouter

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

@router.get("/")
def get_resume():
    return {
        "message": "Resume Router Working"
    }

@router.get("/upload")
def upload_resume():
    return {
        "message": "Resume Uploaded Successfully"
    }