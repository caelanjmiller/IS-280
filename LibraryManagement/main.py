from utilities.users import *
from utilities.books import *
from utilities.exceptions import *
from utilities.transactions import *

def main():
    menu: str = (
    "1. Add Book\n"
    "2. Add User\n"
    "3. List Books\n"
    "4. List Users\n"
    "5. Borrow Book\n"
    "6. Exit\n"
    )

    is_running = True

    while is_running:
        print("Library Management System")
        print("-" * len("Library Management System"))
        print(menu)
        user_choice = input("Select an option: ")
        match user_choice:

            case "1":
                book_id: str = input("Enter book ID: ")
                title: str = input("Enter book title: ")
                author: str = input("Enter book author: ")
                new_book: Book = Book(book_id, title, author, True)
                library.append(new_book)
                print(f"Book '{new_book.title}' added successfully.")
                print()

            case "2":
                user_id: str = input("Enter user ID: ")
                name: str = input("Enter user name: ")
                new_user: User = create_user(user_id, name)
                users.append(new_user)
                print(f"User '{new_user.name}' added successfully.")
                print()

            case "3":
                print()
                list_books(library)
                print()

            case "4":
                print()
                list_users(users)
                print()

            case "5":
                user_id: str = input("Enter user ID: ")
                book_id: str = input("Enter book ID: ")
                print()
                borrow_book(user_id, book_id)
                print()

            case "6":
                print("Exiting the system. Goodbye!")
                is_running = False

if __name__ == "__main__":
    main()