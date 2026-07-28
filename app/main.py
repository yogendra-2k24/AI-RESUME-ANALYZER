from fastapi import FastAPI
from app.routers.resume import router as resume_router

from app.exceptions.custom_exceptions import AppException
from app.exceptions.handler import app_exception_handler

app = FastAPI()

app.add_exception_handler(
    AppException,
    app_exception_handler,
)

@app.get("/")
def home():
    return {"Message": "AI Resume Analyzer API is running"}

app.include_router(resume_router)