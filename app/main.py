from fastapi import FastAPI
from app.routers.resume import router as resume_router

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "AI Resume Analyzer API is running"}

app.include_router(resume_router)