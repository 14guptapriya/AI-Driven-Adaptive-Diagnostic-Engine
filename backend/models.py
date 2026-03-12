from pydantic import BaseModel
from typing import List

class AnswerSubmission(BaseModel):
    session_id: str
    question_id: str
    answer: str