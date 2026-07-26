from pydantic import BaseModel

class ResumeAnalysis(BaseModel):

    ats_score: int
    missing_skills: list[str]
    suggestions: list[str]