
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
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
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
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def list_books(self) -> list:
        """Tüm kitap nesnelerini döner."""
        return self.books

    def find_book(self, isbn: str) -> Book | None:
        """ISBN’e göre Book nesnesini döner ya da None."""
        return next((book for book in self.books if book.isbn == isbn), None)

    def add_book_by_isbn(self, isbn: str) -> bool:
        """Open Library API'den kitap bilgisi alarak ekler."""
        if self.find_book(isbn):
            return False  # Zaten varsa ekleme

        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url)
            if response.status_code != 200:
                return False

            data = response.json()
            title = data.get("title", "Bilinmeyen Başlık")
            authors = data.get("authors", [])
            author_name = "Bilinmeyen Yazar"

            if authors:
                # Yazar bilgisi ayrı bir endpoint'ten alınmalı
                author_key = authors[0].get("key")
                author_url = f"https://openlibrary.org{author_key}.json"
                author_resp = httpx.get(author_url)
                if author_resp.status_code == 200:
                    author_data = author_resp.json()
                    author_name = author_data.get("name", author_name)

            book = Book(title=title, author=author_name, isbn=isbn)
            return self.add_book(book)

        except Exception as e:
            print(f"Hata oluştu: {e}")
            return False

