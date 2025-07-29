class BookNotFoundError(Exception):
    """
    Raised if the book ID does not exist in the system.
    """
    def __init__(self, book_id: str) -> None:
        super().__init__(f"Error: Book ID Does Not Exist")
        self.book_id = book_id

class UserNotFoundError(Exception):
    """
    Raised if the user ID does not exist in the system.
    """
    def __init__(self, user_id: str) -> None:
        super().__init__(f"Error: User ID Does Not Exist")
        self.user_id = user_id

class BookAlreadyBorrowedError(Exception):
    """
    Raised if a user tries to borrow a book they already have.
    """
    def __init__(self, user_id: str, book_id: str) -> None:
        super().__init__(f"Error: User '{user_id}' has already borrowed '{book_id}'.")

class BookNotAvailableError(Exception):
    """
    Raised if the book is unavailable for borrowing.
    """
    def __init__(self, book_id: str) -> None:
        super().__init__(f"Error: Book '{book_id}' is not available for borrowing.")
