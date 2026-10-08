# Lab 5: Modular Multi-Class Architecture & Library Management System
from books import Book
from users import User
from library import Library

if __name__ == "__main__":
    city_library = Library("City Central Library")

    book1 = Book(
        isbn="0001",
        title="Python for dummie",
        author="Carl Marx",
        publisher="Library public"
    )
    book2 = Book(
        isbn="0002",
        title="0 to 100 programing",
        author="Andrew Hunt",
        publisher="el bibliotecario"
    )
    
    user1 = User(
        user_id="01",
        name="Aldo Carrillo",
        pin="1234"
    )
    user2 = User(
        user_id="02",
        name="Jose Emmanuel",
        pin="5678"
    )

    city_library.add_book(book1)
    city_library.add_book(book2)
    city_library.add_user(user1)
    city_library.add_user(user2)

    # 2. Inventory Inspection
    city_library.show_books()

    city_library.borrow_book(isbn="0001", user_id="01")
    city_library.show_books()

    city_library.borrow_book(isbn="0001", user_id="02")

    city_library.return_book(isbn="0001", user_id="U101")

    city_library.show_books()