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

