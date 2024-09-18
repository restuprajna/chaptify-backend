from pydantic import BaseModel
from typing import Optional

class BookCreateSchema(BaseModel):
    title: str
    author: str
    description: str
    is_available: bool = True

class BookResponseSchema(BookCreateSchema):
    title: str
    author: str
    description: str
    is_available: bool = True
