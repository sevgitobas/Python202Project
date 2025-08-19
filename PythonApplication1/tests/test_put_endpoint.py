# -*- coding: utf-8 -*-

import pytest


def test_update_book(client):
    original = {
        "title": "Eski Kitap",
        "author": "Yazar",
        "year": 2000,
        "isbn": "123-8888888888"
    }
    updated = {
        "title": "Güncellenmiş Kitap",
        "author": "Yeni Yazar",
        "year": 2025,
        "isbn": "123-8888888888"
    }

    client.post("/books", json=original)
    response = client.put(f"/books/{original['isbn']}", json=updated)
    assert response.status_code == 200
    assert response.json()["title"] == updated["title"]
    assert response.json()["author"] == updated["author"]

def test_update_nonexistent_book(client):   #olmayan kitabı güncelleme testi
    updated = {
        "title": "Hayali Kitap",
        "author": "Yazar",
        "year": 2025,
        "isbn": "123-0000000000"
    }
    response = client.put("/books/123-0000000000", json=updated)
    assert response.status_code == 404
    assert "bulunamadı" in response.json()["detail"]

