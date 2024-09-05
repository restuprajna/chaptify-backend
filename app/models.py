from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, Union, List
from bson import ObjectId

class BookModel(BaseModel):
    id: Optional[Union[str, ObjectId]] = Field(None, alias="_id") 
    title: str
    author: str
    description: str
    tags: Optional[str] = None
    is_available: bool = True
    formats: List[str] = ["physical", "digital"]  # Both formats available by default
    price: Optional[float] = None  # Price for digital copy
    subscription_required: bool = False  # If the digital version requires a subscription

    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        return str(value) if isinstance(value, ObjectId) else value

    class Config:
        allow_population_by_field_name = True  # Allows use of _id as an alias
        arbitrary_types_allowed = True  # Allows using ObjectId type

class UserModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")  # Alias for MongoDB's _id field
    username: str
    email: str
    is_active: bool = True

    # Validator to convert ObjectId to string
    @field_validator("id", mode="before")
    def convert_object_id(cls, value):
        return str(value) if isinstance(value, ObjectId) else value

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )
