import json
import pytest
from book import Book
from library import Library

@pytest.fixture
def tmp_library(tmp_path):
    # Geçici JSON dosyası
    file = tmp_path / "test_library.json"
    # Başlangıçta boş JSON liste
    file.write_text("[]", encoding="utf-8")
    return Library(str(file))

def test_add_and_find_book(tmp_library):
    lib = tmp_library
    b = Book("Dune", "Frank Herbert", "ISBN-DUNE")
    assert lib.add_book(b) is True
    # Aynı ISBN tekrar eklenemez
    assert lib.add_book(b) is False
    # find_book doğru nesneyi döndürür
    found = lib.find_book("ISBN-DUNE")
    assert found is not None
    assert found.title == "Dune"

def test_remove_book(tmp_library):
    lib = tmp_library
    b = Book("Hamlet", "Shakespeare", "ISBN-HAMLET")
    lib.add_book(b)
    # Silme başarılı mı?
    assert lib.remove_book("ISBN-HAMLET") is True
    # Varolmayan ISBN silinemez
    assert lib.remove_book("ISBN-HAMLET") is False

def test_list_books_and_persistence(tmp_library):
    lib = tmp_library
    b1 = Book("A", "X", "1")
    b2 = Book("B", "Y", "2")
    lib.add_book(b1)
    lib.add_book(b2)

    # Listelemede 2 kitap var mı?
    all_books = lib.list_books()
    assert len(all_books) == 2

    # Dosyaya da yazıldı mı kontrolü
    data = json.loads(open(lib.filename, encoding="utf-8").read())
    isbns = {item["isbn"] for item in data}
    assert isbns == {"1", "2"}

    # Yeni Library örneği ile yükle
    lib2 = Library(lib.filename)
    assert len(lib2.list_books()) == 2
    assert lib2.find_book("1") is not None
    assert lib2.find_book("2") is not None
