# -*- coding: utf-8 -*-

import pytest
from src.api import app


@pytest.fixture
def book_data():
    return {
        "title": "Güncellenecek Kitap",
        "author": "Yazar",
        "year": 2020,
        "isbn": "5555555555"
    }

def test_update_existing_book(client, book_data):
    client.post("/books", json=book_data)

    updated = book_data.copy()
    updated["title"] = "Yeni Başlık"
    updated["year"] = 2025

    response = client.put(f"/books/{book_data['isbn']}", json=updated)
    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Yeni Başlık"
    assert data["year"] == 2025
    assert data["isbn"] == book_data["isbn"]

    response = client.get("/books")
    kitaplar = response.json()
    assert any(book["title"] == "Yeni Başlık" and book["isbn"] == book_data["isbn"] for book in kitaplar)


def test_update_nonexistent_book(client):
    updated = {
        "title": "Olmayan Kitap",
        "author": "Yazar",
        "year": 2025,
        "isbn": "0000000000"
    }
    response = client.put("/books/0000000000", json=updated)
    assert response.status_code == 404
    assert "bulunamadı" in response.json()["detail"].lower()
