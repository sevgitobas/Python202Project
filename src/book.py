# book.py

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def to_dict(self) -> dict:
        """JSON serileştirmesi için sözlüğe çevir."""
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

    @staticmethod
    def from_dict(data: dict):
        """JSON’dan Book nesnesi oluştur."""
        return Book(title=data["title"], author=data["author"], isbn=data["isbn"])
