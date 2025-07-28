from utilities.users import *
from utilities.books import *
from utilities.exceptions import *
from utilities.transactions import *

users: list = []
library: list = []

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
        
        user_choice = input("Select an option: ")

        match user_choice:

            case "1":
                pass

            case "2":
                pass

            case "3":
                list_books(library)

            case "4":
                list_users(users)

            case "5":
                pass

            case "6":
                print("Exiting the system. Goodbye!")
                is_running = False

if __name__ == "__main__":
    main()