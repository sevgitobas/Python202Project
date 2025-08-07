# main.py
print("DEBUG: main.py başladı")


from library import Library
from book import Book


def menu():
    print("DEBUG: Menü fonksiyonu çağrıldı")
    print("\n=== KÜTÜPHANE UYGULAMASI ===")
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitapları Listele")
    print("4. Kitap Ara")
    print("5. Çıkış")

def main():
    lib = Library("library.json")

    while True:
        menu()
        choice = input("Seçiminiz (1-5): ").strip()

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
            isbn = input("Silinecek kitabın ISBN’i: ").strip()
            if lib.remove_book(isbn):
                print("Kitap silindi.")
            else:
                print("ISBN bulunamadı.")

        elif choice == "3":
            books = lib.list_books()
            if not books:
                print("Kütüphane boş.")
            else:
                print("\n--- Kütüphanedeki Kitaplar ---")
                for b in books:
                    print(b)

        elif choice == "4":
            isbn = input("Aranacak ISBN: ").strip()
            result = lib.find_book(isbn)
            if result:
                print("Bulunan kitap:", result)
            else:
                print("Kitap bulunamadı.")

        elif choice == "5":
            print("Programdan çıkılıyor.")
            break

        else:
            print("Geçersiz seçim, lütfen 1-5 arasında bir değer girin.")

if __name__ == "__main__":
    main()