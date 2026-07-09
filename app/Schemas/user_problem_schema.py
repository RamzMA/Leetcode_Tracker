from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from app.Schemas.schemas import ProblemResponse


class UserProblemCreate(BaseModel):
    problem_id: int


class UserProblemUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None
    attempts: Optional[int] = None
    time_spent_minutes: Optional[int] = None
    rating: Optional[int] = None
    favorite: Optional[bool] = None
    solved_at: Optional[datetime] = None


class UserProblemResponse(BaseModel):
    id: int
    status: str
    attempts: int
    favorite: bool
    problem: ProblemResponse

    model_config = {
        "from_attributes": True
    }