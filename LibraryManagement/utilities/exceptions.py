
class BookNotFoundError(Exception):
    """
    Raised if the book ID does not exist in the system.
    """
    pass

class UserNotFoundError(Exception):
    """
    Raised if the user ID does not exist in the system.
    """
    pass

class BookAlreadyBorrowedError(Exception):
    """
    Raised if a user tries to borrow a book they already have.
    """
    pass

class BookNotAvailableError(Exception):
    """
    Raised if the book is unavailable for borrowing.
    """
    pass