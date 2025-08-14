# main.py

import os
from src.library import Library
from src.book import Book
from pathlib import Path


def menu():
    print("\n=== KÜTÜPHANE UYGULAMASI ===")
    print("1. Kitap Ekle (Manuel)")
    print("2. Kitap Ekle (ISBN ile - API)")
    print("3. Kitap Sil")
    print("4. Kitapları Listele")
    print("5. Kitap Ara")
    print("6. Çıkış")

def main():
    base_dir = Path(__file__).resolve().parent
    json_path = base_dir / "data" / "library.json"
    lib = Library(str(json_path))

    while True:
        menu()
        choice = input("Seçiminiz (1-6): ").strip()

        if choice == "1":
            title = input("Kitap başlığı: ").strip()
            author = input("Yazar: ").strip()
            isbn = input("ISBN: ").strip()
            book = Book(title, author, isbn)
            if lib.add_book(book):
                print("Kitap başarıyla eklendi.")
            else:
                print("Bu ISBN zaten mevcut!")

        elif choice == "2":
            isbn = input("ISBN girin: ").strip()
            success = lib.add_book_by_isbn(isbn)
            if success:
                print("Kitap API üzerinden başarıyla eklendi.")
            else:
                print("Kitap eklenemedi. ISBN geçersiz olabilir veya zaten mevcut.")

        elif choice == "3":
            isbn = input("Silinecek kitabın ISBN’i: ").strip()
            if lib.remove_book(isbn):
                print("Kitap silindi.")
            else:
                print("ISBN bulunamadı.")

        elif choice == "4":
            books = lib.list_books()
            if not books:
                print("Kütüphane boş.")
            else:
                print("\n--- Kütüphanedeki Kitaplar ---")
                for b in books:
                    print(b)

        elif choice == "5":
            isbn = input("Aranacak ISBN: ").strip()
            result = lib.find_book(isbn)
            if result:
                print("Bulunan kitap:", result)
            else:
                print("Kitap bulunamadı.")

        elif choice == "6":
            print("Programdan çıkılıyor.")
            break

        else:
            print("Geçersiz seçim, lütfen 1-6 arasında bir değer girin.")

if __name__ == "__main__":
    main()