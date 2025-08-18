# -*- coding: utf-8 -*-


import unittest
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

class TestDeleteEndpoint(unittest.TestCase):

    def setUp(self):
        # Test i�in �rnek kitap ekleyelim
        self.sample_book = {
            "id": "test123",
            "title": "Test Kitab�",
            "author": "Test Yazar",
            "year": 2025
        }
        client.post("/books", json=self.sample_book)

    def test_delete_existing_book(self):
        response = client.delete(f"/books/{self.sample_book['id']}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("silindi", response.json().get("message", "").lower())

    def test_delete_nonexistent_book(self):
        response = client.delete("/books/doesnotexist")
        self.assertEqual(response.status_code, 404)
        self.assertIn("bulunamad�", response.json().get("detail", "").lower())

    def test_delete_with_invalid_id(self):
        response = client.delete("/books/123!")  # Ge�ersiz ID format� varsay�m�
        self.assertEqual(response.status_code, 422)

    def tearDown(self):
        # Temizlik: varsa test kitab�n� sil
        client.delete(f"/books/{self.sample_book['id']}")


if __name__ == "__main__":
    unittest.main()
