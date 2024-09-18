from fastapi import FastAPI
from app.api.endpoints import books, users

app = FastAPI()

app.include_router(books.router, prefix="/api/v2/books", tags=["Books"])
app.include_router(users.router, prefix="/api/v2/users", tags=["Users"])
