from datetime import datetime

from pydantic import BaseModel, ConfigDict

class ResumeHistoryResponse(BaseModel):

    id: int
    filename: str
    ats_score: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)