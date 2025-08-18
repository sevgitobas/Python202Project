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
        encoded_title = quote(self.sample_book['title'])
        response = client.delete(f"/books/{encoded_title}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("silindi", response.json().get("message", "").lower())

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
