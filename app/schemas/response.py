from typing import Any, TypeVar, Generic
from pydantic import BaseModel

T= TypeVar("T")

class SuccessResponse(BaseModel, Generic[T]):
    success: bool=True
    data: T