from fastapi import UploadFile
from pathlib import Path
from app.exceptions.custom_exceptions import InvalidFileTypeException

ALLOWED_EXTENSIONS = {
    ".pdf",
}

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
}

def validate_file(file: UploadFile) -> None:

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise InvalidFileTypeException()

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise InvalidFileTypeException()

    return