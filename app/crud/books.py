from app.models.book import BookModel
from app.schemas.book_schema import BookCreateSchema
from bson import ObjectId
from app.core.database import db
from fastapi import HTTPException

async def create_book(book: BookCreateSchema) -> BookModel:
    existing_book = await db["books"].find_one({"title": book.title})
    if existing_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    
    book_data = book.model_dump()  # Convert Pydantic object to dict
    result = await db["books"].insert_one(book_data)
    new_book = await db["books"].find_one({"_id": result.inserted_id})
    
    return BookModel(**new_book)

async def get_book_by_id(book_id: str) -> BookModel:
    if not ObjectId.is_valid(book_id):
        raise HTTPException(status_code=400, detail="Invalid Book ID")
    book = await db["books"].find_one({"_id": ObjectId(book_id)})
    if not book:
        return None
    return BookModel(**book)
