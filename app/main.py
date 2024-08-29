# main.py
from fastapi import FastAPI, HTTPException
from .models import BookModel, UserModel
from .crud import create_book, get_book_by_id, update_book, delete_book

app = FastAPI()

@app.post("/books/", response_model=BookModel)
async def create_book_endpoint(book: BookModel):
    return await create_book(book)

@app.get("/books/{book_id}", response_model=BookModel)
async def get_book(book_id: str):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=BookModel)
async def update_book_endpoint(book_id: str, book: BookModel):
    updated_book = await update_book(book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{book_id}", response_model=dict)
async def delete_book_endpoint(book_id: str):
    if not await delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
