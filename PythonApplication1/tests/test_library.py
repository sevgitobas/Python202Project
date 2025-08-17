import unittest
import os
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from pathlib import Path
from src.book import Book
import tempfile
from src.library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Geçici dosya oluştur
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.library = Library(self.temp_file.name)
        self.library.books = [
            Book(title="Test Kitabı", author="Test Yazar", isbn="1234567890")
        ]
        self.library.save_books()

    def tearDown(self):
        # Geçici dosyayı sil
        try:
            os.remove(self.temp_file.name)
        except Exception as e:
            print(f"Dosya silinemedi: {e}")

    def test_add_book(self):
        book = Book("Test Kitap", "Test Yazar", "9999999999")
        result = self.library.add_book(book)
        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 1)

    def test_add_duplicate_book(self):
        book1 = Book("Kitap 1", "Yazar", "111")
        book2 = Book("Kitap 2", "Yazar", "111")  # Aynı ISBN
        self.library.add_book(book1)
        result = self.library.add_book(book2)
        self.assertFalse(result)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        book = Book("Silinecek Kitap", "Yazar", "222")
        self.library.add_book(book)
        result = self.library.remove_book("222")
        self.assertTrue(result)
        self.assertEqual(len(self.library.books), 0)

    def test_find_book(self):
        book = Book("Aranacak Kitap", "Yazar", "333")
        self.library.add_book(book)
        found = self.library.find_book("333")
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Aranacak Kitap")

    def test_list_books(self):
        book1 = Book("Kitap A", "Yazar A", "444")
        book2 = Book("Kitap B", "Yazar B", "555")
        self.library.add_book(book1)
        self.library.add_book(book2)
        books = self.library.list_books()
        self.assertEqual(len(books), 2)

    def test_add_book_by_isbn(self):
        isbn = "9780140328721"  # Matilda by Roald Dahl
        result = self.library.add_book_by_isbn(isbn)
        self.assertTrue(result)
        book = self.library.find_book(isbn)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Matilda")

    def test_remove_book_by_isbn(self):
        book = Book("Test Kitap", "Test Yazar", "1234567890")
        self.library.add_book(book)

        # Silme işlemi
        result = self.library.remove_book("1234567890")
        self.assertTrue(result)

        # Tekrar silmeye çalış → False dönmeli
        result = self.library.remove_book("1234567890")
        self.assertFalse(result)

        # Kitap gerçekten silinmiş mi?
        self.assertEqual(len(self.library.books), 0)

if __name__ == "__main__":
    unittest.main()
