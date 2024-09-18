from fastapi import APIRouter
from app.crud.users import create_user
from app.schemas.user_schema import UserCreateSchema, UserResponseSchema

router = APIRouter()

@router.post("/", response_model=UserResponseSchema)
async def create_new_user(user: UserCreateSchema):
    return await create_user(user)
