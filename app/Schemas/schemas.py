from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str

    model_config = {
        'from_attributes': True
    }

class ProblemCreate(BaseModel):
    title: str
    difficulty: str
    status: str
    topic: str

class UserProblemResponse(BaseModel):
    id: int
    status: str
    attempts: int
    favorite: bool
    problem: ProblemResponse

    class Config:
        from_attributes = True
