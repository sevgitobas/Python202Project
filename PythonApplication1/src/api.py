from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.routers import users, books
from src.models.book import Book
from src.db import books_db  

app = FastAPI()
app.include_router(users.router)
app.include_router(books.router)

@app.post("/books")
def add_book(book: Book):
    if any(b.title == book.title and b.author == book.author for b in books_db):
        return {"message": "Bu kitap zaten mevcut", "book": book}
    books_db.append(book)
    return {"message": "Kitap başarıyla eklendi", "book": book}

@app.get("/books", response_model=List[Book])
def list_books():
    return books_db

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    for book in books_db:
        if book.isbn == isbn:
            books_db.remove(book)
            return {"message": f"{book.title} kitabı silindi"}
    raise HTTPException(status_code=404, detail=f"{isbn} ISBN'li kitap bulunamadı")
