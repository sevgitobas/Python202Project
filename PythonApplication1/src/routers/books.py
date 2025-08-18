# -*- coding: utf-8 -*-

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from src.models.book import Book
from src.db import books_db

router = APIRouter()


@router.post("/books")
def add_book(book: Book):
    books_db.append(book)
    return {"message": "Kitap başarıyla eklendi", "book": book}
