# -*- coding: utf-8 -*-

import unittest
from fastapi.testclient import TestClient
from src.api import app

class TestBookEndpoints(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_add_book(self):
        payload = {"title": "1984", "author": "George Orwell", "year": 1949}
        response = self.client.post("/books", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Kitap başarıyla eklendi", response.json()["message"])

    def test_list_books(self):
        response = self.client.get("/books")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == "__main__":
    unittest.main()
