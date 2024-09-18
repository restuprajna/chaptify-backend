from fastapi import APIRouter, HTTPException
from app.crud.books import create_book, get_book_by_id
from app.schemas.book_schema import BookCreateSchema, BookResponseSchema
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=BookCreateSchema)
async def create_new_book(book: BookCreateSchema):
    try:
        new_book = await create_book(book)
        return new_book
    except HTTPException as e:
        raise HTTPException(status_code=400, detail="Book already exists")

@router.get("/{book_id}", response_model=BookResponseSchema)
async def get_book(book_id: str):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
