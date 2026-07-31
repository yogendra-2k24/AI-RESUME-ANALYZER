from enum import Enum

class SortField(str, Enum):
    CREATED_AT = "created_at"
    ATS_SCORE = "ats_score"

class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"