from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    tags: Optional[str] = None

class BookOut(BookCreate):
    id: str
    is_available: bool

class UserCreate(BaseModel):
    email: str
    is_admin: bool = False
