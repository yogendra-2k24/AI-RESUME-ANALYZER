from fastapi import UploadFile

from app.services.pdf_service import extract_text
from app.services.storage_service import save_file
from app.services.ai_service import analyze_text
from app.schemas.resume_analysis import ResumeAnalysis
from app.validators.file_validator import validate_file
from app.core.logger import logger

# building service for resume upload router

def analyze_resume(file: UploadFile) -> ResumeAnalysis:

    logger.info("Resume analysis started")

    validate_file(file)

    logger.info("File validation successful")

    file_path = save_file(file)

    logger.info("File saved successfully")

    text = extract_text(file_path)

    logger.info("PDF text extracted successfully")

    logger.info("Starting resume analysis using Gemini")

    analysis = analyze_text(text)

    logger.info("Resume analysis completed successfully")

    return analysis
    