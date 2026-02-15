from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    full_name: str
    email: EmailStr
    hashed_password: str
    role: str = "user"  # mặc định là user


class Question(BaseModel):
    title: str
    question_type: str  # multiple_choice, fill_blank, boolean
    content: str
    options: list[str] = []
    correct_answer: str
    explanation: Optional[str] = None
    difficulty: float = 0.5
    topic: str
    status: str = "DRAFT"  # DRAFT, PUBLISHED
    created_at: Optional[str] = None
