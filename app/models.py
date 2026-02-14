from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    full_name: str
    email: EmailStr
    hashed_password: str
    role: str = "user"  # mặc định là user

