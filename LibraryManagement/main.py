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
                pass

            case "4":
                pass

            case "5":
                pass

            case "6":
                print("Exiting the system. Goodbye!")
                is_running = False

if __name__ == "__main__":
    main()