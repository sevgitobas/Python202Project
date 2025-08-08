import pytest
from book import Book

def test_str_method():
    b = Book("Ulysses", "James Joyce", "978-0199535675")
    assert str(b) == "Ulysses by James Joyce (ISBN: 978-0199535675)"

def test_to_dict_and_from_dict():
    b1 = Book("1984", "George Orwell", "12345")
    d = b1.to_dict()
    # to_dict doğru anahtarları dönüyor mu?
    assert d == {"title": "1984", "author": "George Orwell", "isbn": "12345"}
    # from_dict ile nesne tekrar oluşturulsun
    b2 = Book.from_dict(d)
    assert isinstance(b2, Book)
    assert b2.title == b1.title
    assert b2.author == b1.author
    assert b2.isbn == b1.isbn
