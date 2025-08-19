# -*- coding: utf-8 -*-

import pytest
import os
import tempfile
from unittest.mock import patch, MagicMock
from src.models.book import Book
from src.library import Library

@pytest.fixture
def temp_library():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    library = Library(filename=temp_file.name)
    library.books = []
    library.save_books()
    yield library
    temp_file.close()
    os.remove(temp_file.name)

def test_add_book(temp_library):
    book = Book(title="Test Kitap", author="Test Yazar", year=2020, isbn="123-1234567890")
    result = temp_library.add_book(book)
    assert result is True
    assert len(temp_library.books) == 1

def test_add_duplicate_book(temp_library):
    book1 = Book(title="Kitap 1", author="Yazar", year=2020, isbn="111-1111111111")
    book2 = Book(title="Kitap 2", author="Yazar", year=2021, isbn="111-1111111111")
    temp_library.add_book(book1)
    result = temp_library.add_book(book2)
    assert result is False
    assert len(temp_library.books) == 1

def test_remove_book(temp_library):
    book = Book(title="Silinecek Kitap", author="Yazar", year=2022, isbn="222-2222222222")
    temp_library.add_book(book)
    result = temp_library.remove_book("222-2222222222")
    assert result is True
    assert len(temp_library.books) == 0

def test_find_book(temp_library):
    book = Book(title="Aranacak Kitap", author="Yazar", year=2023, isbn="333-3333333333")
    temp_library.add_book(book)
    found = temp_library.find_book("333-3333333333")
    assert found is not None
    assert found.title == "Aranacak Kitap"

def test_list_books(temp_library):
    book1 = Book(title="Kitap A", author="Yazar A", year=2020, isbn="444-4444444444")
    book2 = Book(title="Kitap B", author="Yazar B", year=2021, isbn="555-5555555555")
    temp_library.add_book(book1)
    temp_library.add_book(book2)
    books = temp_library.list_books()
    assert len(books) == 2

def test_add_book_by_isbn(temp_library):
    with patch("src.library.httpx.get") as mock_get:
        book_response = MagicMock()
        book_response.status_code = 200
        book_response.json.return_value = {
            "title": "Matilda",
            "authors": [{"key": "/authors/OL34184A"}]
        }

        author_response = MagicMock()
        author_response.status_code = 200
        author_response.json.return_value = {
            "name": "Roald Dahl"
        }

        mock_get.side_effect = [book_response, author_response]

        isbn = "978-0140328721"
        result = temp_library.add_book_by_isbn(isbn)
        assert result is True

        book = temp_library.find_book(isbn)
        assert book is not None
        assert book.title == "Matilda"
        assert book.author == "Roald Dahl"

def test_remove_book_by_isbn(temp_library):
    book = Book(title="Test Kitap", author="Test Yazar", year=2020, isbn="123-1234567890")
    temp_library.add_book(book)

    result = temp_library.remove_book("123-1234567890")
    assert result is True

    result = temp_library.remove_book("123-1234567890")
    assert result is False

    assert len(temp_library.books) == 0
