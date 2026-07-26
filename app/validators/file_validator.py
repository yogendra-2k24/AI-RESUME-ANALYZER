from fastapi import UploadFile
from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".pdf",
}

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
}

def validate_file(file: UploadFile) -> None:

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError("Only PDF files are allowed")

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise ValueError("Invalid contenet type")