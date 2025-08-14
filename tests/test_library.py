import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pathlib import Path
from src.book import Book
from src.library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Test için ayrı bir dosya kullanıyoruz
        base_dir = Path(__file__).resolve().parent
        self.test_file = base_dir / "test_library.json"
        self.library = Library(str(self.test_file))
        self.library.books = []
        self.library.save_books()

    def tearDown(self):
        # Test dosyasını sil
        if self.test_file.exists():
            self.test_file.unlink()

    def test_add_book(self):
        book = Book("Test Kitap", "Test Yazar", "1234567890")
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

if __name__ == "__main__":
    unittest.main()
