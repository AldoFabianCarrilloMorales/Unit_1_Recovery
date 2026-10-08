from books import Book

class User:
    def __init__(self, user_id: str, name: str, pin: str):
        self.user_id = user_id
        self.name = name
        self.pin = pin
        self.borrowed_books: List['Book'] = []

    def borrow(self, book: 'Book') -> None:
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)

    def return_book(self, book: 'Book') -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self) -> str:
        return f"User ID: {self.user_id} | Name: {self.name} | Active Loans: {len(self.borrowed_books)}"