# -*- coding: utf-8 -*-

import pytest
import time


@pytest.fixture
def test_user_id():
    return int(time.time())

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user(client, test_user_id):
    payload = {"id": test_user_id, "name": "Sevgi"}
    response = client.post("/users", json=payload)
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Kullanıcı oluşturuldu" in response.json()["message"]

def test_cleanup_user(client, test_user_id):
    response = client.delete(f"/users/{test_user_id}")
    assert response.status_code in [200, 404] 