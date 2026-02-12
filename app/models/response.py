from typing import List
from pydantic import BaseModel

class CandidateResult(BaseModel):
    candidate_name: str
    final_match_percentage: float
    recommendation: str
    matched_skills: List[str]
    missing_skills: List[str]
