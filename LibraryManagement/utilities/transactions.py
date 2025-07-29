from utilities.users import users
from utilities.books import library
from utilities.exceptions import *

def borrow_book(user_id, book_id):
    """Borrow a book for a particular user"""
    try:
        # Fetch 1st match of user_id; passed argument
        selected_user = next((user for user in users if user.user_id == user_id), None)
        if not selected_user:
            raise UserNotFoundError(user_id)
        
        # Same, but with book
        selected_book = next((book for book in library if book.book_id == book_id), None)
        if not selected_book:
            raise BookNotFoundError(book_id)
        
        if selected_book in selected_user.borrowed_books:
            raise BookAlreadyBorrowedError(user_id, book_id)

        if not selected_book.available:
            raise BookNotAvailableError(book_id)

        selected_user.borrowed_books.append(book_id)
        selected_book.available = False
        print(f"Book '{book_id}' successfully borrowed.")

    except (
        BookNotFoundError,
        UserNotFoundError,
        BookAlreadyBorrowedError,
        BookNotAvailableError
    ) as e:
        print(e)