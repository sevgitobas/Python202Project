# -*- coding: utf-8 -*-

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Book(BaseModel):
    title: str
    author: str
    year: int

books_db: List[Book] = []

@router.post("/books")
def add_book(book: Book):
    books_db.append(book)
    return {"message": "Kitap başarıyla eklendi", "book": book}
