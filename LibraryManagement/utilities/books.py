class Book:
    def __init__(self, book_id: str, title: str, author: str, available: bool) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available


def list_books(library: list):
    """
    Print formatted list of books with their info
    """
    print(f"Library Books:")
    print(f"{'ID':<10}{'Title':<31}{'Author':<20}{'Available'}")
    print("-" * 75)
    for book in library:
        print(f"{book.book_id:<10}{book.title:<30}{book.author:<20}{str(book.available)}")

library: list = []