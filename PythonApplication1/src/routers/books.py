# -*- coding: utf-8 -*-

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from src.models.book import Book
from src.db import books_db

router = APIRouter()


@router.post("/books", response_model=Book, status_code=201)
def add_book(book: Book):
    if any(b.isbn == book.isbn for b in books_db):
        return JSONResponse(
            status_code=409,
            content={"message": "Bu ISBN zaten mevcut", "book": book.model_dump()}
        )
    books_db.append(book)
    return book

@router.get("/books", response_model=List[Book])
def list_books():
    return books_db

@router.get("/books/{isbn}", response_model=Book)
def get_book_by_isbn(isbn: str):
    for book in books_db:
        if book.isbn == isbn:
            return book
    raise HTTPException(status_code=404, detail="Kitap bulunamadı")

@router.delete("/books/{isbn}", status_code=200)
def delete_book(isbn: str):
    for book in books_db:
        if book.isbn == isbn:
            books_db.remove(book)
            return {"message": f"{book.title} kitabı silindi"}
    raise HTTPException(status_code=404, detail=f"{isbn} ISBN'li kitap bulunamadı")

@router.put("/books/{isbn}", response_model=Book)
def update_book(isbn: str, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.isbn == isbn:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Kitap bulunamadı.")




