import unittest
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

class TestUserEndpoints(unittest.TestCase):

    def test_get_users(self):
        response = client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_user(self):
        payload = {"id": 2, "name": "Sevgi"}
        response = client.post("/users", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Kullanıcı oluşturuldu", response.json()["message"])

if __name__ == "__main__":
    unittest.main()