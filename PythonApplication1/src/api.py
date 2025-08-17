from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.routers import users, books

app = FastAPI()
app.include_router(users.router)
app.include_router(books.router)

# Kitap modeli
class Book(BaseModel):
    title: str
    author: str
    year: int

# Kitapları saklayacağımız liste
books_db: List[Book] = []

# Kitap ekleme endpoint'i
@app.post("/books")
def add_book(book: Book):
    if any(b.title == book.title and b.author == book.author for b in books_db):
        return {"message": "Bu kitap zaten mevcut", "book": book}
    books_db.append(book)
    return {"message": "Kitap başarıyla eklendi", "book": book}

# Kitapları listeleme endpoint'i
@app.get("/books", response_model=List[Book])
def list_books():
    return books_db

# Kitap silme endpoint'i
@app.delete("/books/{title}")
def delete_book(title: str):
    global books_db
    for book in books_db:
        if book.title == title:
            books_db.remove(book)
            return {"message": f"{title} kitabı silindi"}
    return {"message": f"{title} kitabı bulunamadı"}