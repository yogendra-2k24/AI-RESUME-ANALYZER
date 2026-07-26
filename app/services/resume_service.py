from fastapi import UploadFile

from app.services.pdf_service import extract_text
from app.services.storage_service import save_file
from app.services.ai_service import analyze_text
from app.schemas.resume_analysis import ResumeAnalysis

# building service for resume upload router

def analyze_resume(file: UploadFile) -> ResumeAnalysis:

    file_path = save_file(file)

    text = extract_text(file_path)

    analysis = analyze_text(text)

    return analysis
    