# crud.py
from .models import BookModel, UserModel
from bson import ObjectId
from .database import db
import hashlib
from pymongo.errors import DuplicateKeyError, PyMongoError
from fastapi import HTTPException

async def create_book(book: BookModel) -> BookModel:
    try:
        # Generate a consistent ID based on the title, author, and description
        unique_string = f"{book.title}-{book.author}-{book.description}"
        book_id = hashlib.sha256(unique_string.encode('utf-8')).hexdigest()

        # Assign the generated ID to the book
        book.id = book_id

        # Check if the book already exists
        existing_book = await db["books"].find_one({"_id": book.id})
        if existing_book:
            raise HTTPException(status_code=409, detail="Book already exists with this ID.")

        # Insert the new book
        await db["books"].insert_one(book.model_dump(by_alias=True))
        return book

    
    except PyMongoError as e:
        # This catches other potential errors related to MongoDB operations
        raise HTTPException(status_code=500, detail=f"An error occurred while accessing the database: {str(e)}")

    except Exception as e:
        # General error handling for unexpected issues
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

async def get_book_by_id(book_id: str) -> BookModel:
    book = await db["books"].find_one({"_id": str(book_id)})
    if book:
        return BookModel(**book)
    return None

async def update_book(book_id: str, book: BookModel) -> BookModel:
    await db["books"].update_one({"_id": ObjectId(book_id)}, {"$set": book.model_dump(by_alias=True)})
    updated_book = await db["books"].find_one({"_id": ObjectId(book_id)})
    if updated_book:
        return BookModel(**updated_book)
    return None

async def delete_book(book_id: str) -> bool:
    result = await db["books"].delete_one({"_id": ObjectId(book_id)})
    return result.deleted_count > 0

