import shutil
from app.services.pdf_service import extract_text
from app.services.storage_service import save_file

# building service for resume upload router

def upload_resume_service(file):

    file_path = save_file(file)

    text = extract_text(file_path)

    return{
        "message": "Resume uploaded successfully",
        "file": file.filename,
        "text": text
    }