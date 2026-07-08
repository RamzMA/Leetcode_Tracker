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

class ProblemResponse(ProblemCreate):
    id: int

    model_config = {
        'from_attributes': True
    }
