from pydantic import BaseModel

class Problem(BaseModel):
    title: str
    difficulty: str
    status: str
    topic: str

class Stats(BaseModel):
    total: int
    easy: int
    medium: int
    hard: int
 