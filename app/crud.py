# crud.py
from .models import BookModel, UserModel
from bson import ObjectId
from .database import db

async def create_book(book: BookModel) -> BookModel:
    try:
        book_dict = book.model_dump(by_alias=True)  # Convert Pydantic model to dictionary
        result = await db["books"].insert_one(book_dict)
        created_book = await db["books"].find_one({"_id": result.inserted_id})
        return BookModel(**created_book)  # Automatically converts ObjectId to str
    except Exception as e:
        print(f"Error creating book: {e}")
        raise

async def get_book_by_id(book_id: str) -> BookModel:
    book = await db["books"].find_one({"_id": ObjectId(book_id)})
    if book:
        return BookModel(**book)
    return None

async def update_book(book_id: str, book: BookModel) -> BookModel:
    await db["books"].update_one({"_id": ObjectId(book_id)}, {"$set": book.dict(by_alias=True)})
    updated_book = await db["books"].find_one({"_id": ObjectId(book_id)})
    if updated_book:
        return BookModel(**updated_book)
    return None

async def delete_book(book_id: str) -> bool:
    result = await db["books"].delete_one({"_id": ObjectId(book_id)})
    return result.deleted_count > 0
