

class AppException(Exception):
    def __init__(self, message: str, error_code: str):
       self.message = message
       self.error_code = error_code

       super().__init__(message)

class InvalidFileTypeException(AppException):

    def __init__(self):
        super().__init__(
            message="Only PDF files are allowed",
            error_code="INVALID_FILE_TYPE"
        )