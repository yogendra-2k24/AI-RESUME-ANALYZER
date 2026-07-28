from fastapi import UploadFile

from app.services.pdf_service import extract_text
from app.services.storage_service import save_file
from app.services.ai_service import analyze_text
from app.schemas.resume_analysis import ResumeAnalysis
from app.validators.file_validator import validate_file
from app.core.logger import logger

# building service for resume upload router

def analyze_resume(file: UploadFile) -> ResumeAnalysis:

    logger.info(f"Resume analysis started for '{file.filename}'")

    validate_file(file)

    logger.info(f"File validation successfull for '{file.filename}'")

    file_path = save_file(file)

    logger.info(f"File '{file.filename}' saved successfully")

    text = extract_text(file_path)

    logger.info(f"PDF text extracted successfully from '{file.filename}'")

    logger.info(f"Starting resume analysis using Gemini for '{file.filename}'")

    analysis = analyze_text(text)

    logger.info(f"Resume analysis completed successfully for '{file.filename}'")

    return analysis
    