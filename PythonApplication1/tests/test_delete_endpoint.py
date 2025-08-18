# -*- coding: utf-8 -*-


import unittest
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

class TestDeleteEndpoint(unittest.TestCase):

    def setUp(self):
        # Test için örnek kitap ekleyelim
        self.sample_book = {
            "id": "test123",
            "title": "Test Kitabý",
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
        self.assertIn("bulunamadý", response.json().get("detail", "").lower())

    def test_delete_with_invalid_id(self):
        response = client.delete("/books/123!")  # Geçersiz ID formatý varsayýmý
        self.assertEqual(response.status_code, 422)

    def tearDown(self):
        # Temizlik: varsa test kitabýný sil
        client.delete(f"/books/{self.sample_book['id']}")


if __name__ == "__main__":
    unittest.main()
