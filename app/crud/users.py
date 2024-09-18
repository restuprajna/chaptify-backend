from app.models.user import UserModel
from app.schemas.user_schema import UserCreateSchema
from app.core.database import db

async def create_user(user: UserCreateSchema) -> UserModel:
    user_data = user.model_dump()
    result = await db["users"].insert_one(user_data)
    new_user = await db["users"].find_one({"_id": result.inserted_id})
    return UserModel(**new_user)
