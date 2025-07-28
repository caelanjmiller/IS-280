from exceptions import *

class User:
    def __init__(self, name: str, user_id: str, borrowed_books: list) -> None:
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book_id: str):
        try:
            self.borrowed_books.append(book_id)
        except BookNotFoundError:
            pass