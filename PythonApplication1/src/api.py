from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

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
    books_db.append(book)
    return {"message": "Kitap başarıyla eklendi", "book": book}
