from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    username: str
    email: str

class UserResponseSchema(UserCreateSchema):
    id: str
