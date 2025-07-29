class User:
    def __init__(self, name: str, user_id: str, borrowed_books: list) -> None:
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

def list_users(users: list):
    """
    Print formatted list of users with their borrowed books
    """
    print(f"Registered Users:")
    print(f"{'ID':<10}{'Name':<25}{'Borrowed Books'}")
    print("-" * 60)
    for user in users:
        if user.borrowed_books:
            books: str = ", ".join(user.borrowed_books)
        else:
            books = "None"
        print(f"{user.user_id:<10}{user.name:<25}{books}")

def create_user(user_id: str, name: str) -> User:
    """Create a new library user"""
    user: User = User(name, user_id, [])
    return user

users: list = []