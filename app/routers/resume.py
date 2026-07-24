from fastapi import APIRouter

router = APIRouter()

@router.get("/resume")
def get_resume():
    return {
        "message": "Resume Router Working"
    }

@router.get("/health")
def get_health():
    return {
        "status": "API Running"
    }