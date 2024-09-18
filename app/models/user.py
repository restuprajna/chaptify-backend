from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, Union

class UserModel(BaseModel):
    id: Optional[Union[str, ObjectId]] = Field(None, alias="_id")
    username: str
    email: str
    is_active: bool = True

    class Config:
        arbitrary_types_allowed = True
