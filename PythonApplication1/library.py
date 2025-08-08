
# library.py

import json
import os
from book import Book

class Library:
    def __init__(self, filename: str = "library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

        self.books = [Book.from_dict(item) for item in data]

    def save_books(self):
        """Mevcut kitap listesini JSON dosyasına yazar."""
        with open(self.filename, "w", encoding="utf-8") as f:
            data = [book.to_dict() for book in self.books]
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_book(self, book: Book) -> bool:
        """Yeni kitabı ekler. Aynı ISBN varsa eklemez."""
        if any(b.isbn == book.isbn for b in self.books):
            return False
        self.books.append(book)
        self.save_books()
        return True

    def remove_book(self, isbn: str) -> bool:
        """ISBN’e göre kitabı siler."""
        for i, b in enumerate(self.books):
            if b.isbn == isbn:
                del self.books[i]
                self.save_books()
                return True
        return False

    def list_books(self) -> list:
        """Tüm kitap nesnelerini döner."""
        return self.books

    def find_book(self, isbn: str):
        """ISBN’e göre Book nesnesini döner ya da None."""
        return next((b for b in self.books if b.isbn == isbn), None)

