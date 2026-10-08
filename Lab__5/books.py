class Book:
    def __init__(self, isbn: str, title: str, author: str, publisher: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_available = True 

    def mark_as_borrowed(self) -> None:
        self.is_available = False

    def mark_as_returned(self) -> None:
        self.is_available = True

    def __str__(self) -> str:
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.isbn}] '{self.title}' by {self.author} ({self.publisher}) - {status}"