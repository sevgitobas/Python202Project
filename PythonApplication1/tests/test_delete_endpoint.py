# -*- coding: utf-8 -*-

import pytest
from src.api import app
from src.db import books_db


@pytest.fixture(autouse=True)
def clear_books_db():
    books_db.clear()

@pytest.fixture
def sample_book(client):
    book = {
        "title": "Test Kitabı",
        "author": "Test Yazar",
        "year": 2025
    }
    client.post("/books", json=book)
    yield book
    client.delete(f"/books/{book.get('isbn', book['title'])}")

def test_delete_existing_book(client):
    isbn = "1234567890"
    book = {
        "title": "Silinecek Kitap",
        "author": "Test Yazar",
        "year": 2020,
        "isbn": isbn
    }

    response = client.post("/books", json=book)
    assert response.status_code in [200, 201]

    response = client.delete(f"/books/{isbn}")
    assert response.status_code == 200

    response = client.get("/books")
    kitaplar = response.json()
    assert not any(b.get("isbn") == isbn for b in kitaplar)

def test_delete_nonexistent_book(client):
    response = client.delete("/books/doesnotexist")
    assert response.status_code == 404
    assert "bulunamadı" in response.json().get("detail", "").lower()

def test_delete_with_invalid_title(client):
    response = client.delete("/books/")
    assert response.status_code == 405
