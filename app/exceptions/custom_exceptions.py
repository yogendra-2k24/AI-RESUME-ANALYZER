

class AppException(Exception):
    """Base class for all buisness exceptions."""

    def __init__(self, message: str, error_code: str):
        self.message = message
        self.error_code = error_code
        
        super().__init__(message)