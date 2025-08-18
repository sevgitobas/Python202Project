# -*- coding: utf-8 -*-

import unittest
import time
from fastapi.testclient import TestClient
from src.api import app


class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.test_id = int(time.time())

    def test_get_users(self):
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_user(self):
        payload = {"id": self.test_id, "name": "Sevgi"}
        response = self.client.post("/users", json=payload)
        self.assertIn("message", response.json())
        self.assertIn("Kullanıcı oluşturuldu", response.json()["message"])

    def tearDown(self):
        self.client.delete(f"/users/{self.test_id}")

if __name__ == "__main__":
    unittest.main()