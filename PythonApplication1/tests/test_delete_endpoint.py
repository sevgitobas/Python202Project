# -*- coding: utf-8 -*-


import unittest
from fastapi.testclient import TestClient
from src.api import app, books_db  
from urllib.parse import quote


client = TestClient(app)

class TestDeleteEndpoint(unittest.TestCase):

    def setUp(self):
        books_db.clear()

        # Test için örnek kitap ekleyelim
        self.sample_book = {
            "title": "Test Kitabı",
            "author": "Test Yazar",
            "year": 2025
        }
        client.post("/books", json=self.sample_book)


    def test_delete_existing_book(self):
        isbn = "1234567890"

        # Kitap ekle
        response = client.post("/books", json={
            "title": "Silinecek Kitap",
            "author": "Test Yazar",
            "year": 2020,
            "isbn": isbn
        })
        assert response.status_code == 200 or response.status_code == 201

        # Kitabı sil
        response = client.delete(f"/books/{isbn}")
        self.assertEqual(response.status_code, 200)

        # Silindi mi kontrol et
        response = client.get("/books")
        kitaplar = response.json()
        self.assertFalse(any(book["isbn"] == isbn for book in kitaplar))

    def test_delete_nonexistent_book(self):
        response = client.delete("/books/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertIn("bulunamadı", response.json().get("detail", "").lower())

    def test_delete_with_invalid_title(self):
        response = client.delete("/books/")
        self.assertEqual(response.status_code, 405)

    def tearDown(self):
        client.delete(f"/books/{self.sample_book['title']}")


if __name__ == "__main__":
    unittest.main()
