from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class QuestionCreate(BaseModel):
    title: str
    question_type: str
    content: str
    options: list[str]
    correct_answer: str
    explanation: str | None = None
    difficulty: float
    topic: str
    status: str
