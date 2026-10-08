from typing import List, Optional
from books import Book
from users import User


class Library:
    def __init__(self, name: str = "Central Library"):
        self.name = name
        self.catalog: List[Book] = []
        self.members: List[User] = []

    def add_book(self, book: Book) -> None:
        self.catalog.append(book)
        print(f"[CATALOG] Added book: '{book.title}' (ISBN: {book.isbn})")

    def add_user(self, user: User) -> None:
        self.members.append(user)
        print(f"[MEMBER] Registered user: {user.name} (ID: {user.user_id})")

    def _find_book(self, isbn: str) -> Optional[Book]:
        for book in self.catalog:
            if book.isbn == isbn:
                return book
        return None

    def _find_user(self, user_id: str) -> Optional[User]:
        for user in self.members:
            if user.user_id == user_id:
                return user
        return None

    def show_books(self) -> None:
        print(f" {self.name.upper()} - CATALOG INVENTORY")
        if not self.catalog:
            print(" No books currently in the catalog.")
        else:
            for book in self.catalog:
                status_str = "AVAILABLE" if book.is_available else "CHECKED OUT"
                print(f" • [{book.isbn}] '{book.title}' by {book.author} -> [{status_str}]")

    def borrow_book(self, isbn: str, user_id: str) -> bool:
        book = self._find_book(isbn)
        user = self._find_user(user_id)

        if not book:
            print(f"[ERROR] Transaction failed: Book with ISBN '{isbn}' not found.")
            return False

        if not user:
            print(f"[ERROR] Transaction failed: User with ID '{user_id}' not found.")
            return False

        if not book.is_available:
            print(f"[RESTRICTION WARNING] Cannot borrow '{book.title}' (ISBN: {isbn}). It is currently checked out by another user!")
            return False

        book.mark_as_borrowed()
        user.borrow(book)
        print(f"[SUCCESS] '{book.title}' successfully checked out to {user.name}.")
        return True

    def return_book(self, isbn: str, user_id: str) -> bool:
        book = self._find_book(isbn)
        user = self._find_user(user_id)

        if not book or not user:
            print("[ERROR] Return failed: Invalid ISBN or User ID.")
            return False

        if book not in user.borrowed_books:
            print(f"[WARNING] Return failed: '{book.title}' is not listed under {user.name}'s active loans.")
            return False

        book.mark_as_returned()
        user.return_book(book)
        print(f"[SUCCESS] '{book.title}' successfully returned by {user.name}.")
        return True