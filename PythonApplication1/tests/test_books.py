# -*- coding: utf-8 -*-

import pytest
from fastapi.testclient import TestClient
from src.api import app
from src.db import books_db

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clear_books_db():
    books_db.clear()

def test_add_book(client):
    payload = {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "isbn": "123-1234567890"
    }
    response = client.post("/books", json=payload)
    assert response.status_code == 201
    assert response.json()["isbn"] == payload["isbn"]

def test_delete_book(client):
    payload = {
        "title": "Silinecek Kitap",
        "author": "Test",
        "year": 2020,
        "isbn": "123-1234567890"
    }
    client.post("/books", json=payload)
    response = client.delete(f"/books/{payload['isbn']}")
    assert response.status_code == 200
    assert "silindi" in response.json()["message"]

def test_delete_nonexistent_book(client):
    response = client.delete("/books/0000000000")
    assert response.status_code == 404
    assert "bulunamadı" in response.json()["detail"]

def test_list_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_book_missing_isbn(client): #eksik isbn ile kitap ekleme testi
    payload = {
        "title": "Hayvan Çiftliği",
        "author": "George Orwell",
        "year": 1945
        # isbn eksik
    }
    response = client.post("/books", json=payload)
    assert response.status_code == 422  

def test_add_book_empty_title(client):   #boş başlık ile kitap ekleme testi
    payload = {
        "title": "",
        "author": "George Orwell",
        "year": 1945,
        "isbn": "123-1234567890"
    }
    response = client.post("/books", json=payload)
    assert response.status_code == 422

def test_add_book_duplicate_isbn(client):     #aynı isbn ile kitap ekleme testi
    payload = {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "isbn": "123-1234567890"
    }
    # İlk ekleme
    response1 = client.post("/books", json=payload)
    assert response1.status_code == 201
    # İkinci ekleme
    response2 = client.post("/books", json=payload)
    assert response2.status_code == 409