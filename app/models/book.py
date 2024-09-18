from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, Union

class BookModel(BaseModel):
    id: Optional[Union[str, ObjectId]] = Field(None, alias="_id")
    title: str
    author: str
    description: str
    is_available: bool = True

    class Config:
        arbitrary_types_allowed = True
