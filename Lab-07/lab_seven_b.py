import csv

contacts = []

def main():
    if load_contacts("contacts.csv"):
        print("Contacts loaded successfully.")
    print()
    dont_exit: bool = True
    menu: str = (
    "1. Add Contact\n"
    "2. View Contacts\n"
    "3. Search Contacts\n"
    "4. Delete Contact\n"
    "5. Exit"    
    )
    while dont_exit:
        print(menu)
        choice: str = input("Enter choice: ")
        match choice:
            case "1":
                contact: dict = add_contact()
                contacts.append(contact)
                save_to_csv()
                load_contacts("contacts.csv")
                print()
            case "2":
                view_contacts(contacts)
            case "3":
                search_contacts()
            case "4":
                index: int = int(input("Enter contact number to delete: ")) - 1
                delete_contacts(index)
                save_to_csv()
                print(f"Contact deleted successfully.")
                print()
            case "5":
                print(f"Exiting...")
                dont_exit: bool = False
            case _:
                print(f"Invalid choice. Please enter a number from 1 to 5.")

def add_contact():
    name: str = input("Enter name: ")
    email: str = input("Enter email: ")
    phone_number: str = input("Enter phone number: ")
    return {
        'name': name,
        'email': email,
        'phone': phone_number
    }

def load_contacts(filename):
    try:
        contacts.clear()
        with open(filename, 'r') as csv_file:
            file_contents = csv.DictReader(csv_file, fieldnames=['name', 'email', 'phone'])
            for contact in file_contents:
                contacts.append(contact)
        return True
    except FileNotFoundError:
        print(f"CSV file not found. A new file will be created when adding contacts.")
        return False

def view_contacts(contacts: list):
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['email']} - {contact['phone']}")
    print()

def search_contacts():
    name_to_search: str = input("Enter the name to search for: ")
    for contact in contacts:
        if name_to_search in contact.values():
            print(f"Found contact: Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")
            print()
            break
    else:
        print(f"Contact not found.")

def save_to_csv():
    try:
        with open("contacts.csv", "w") as csv_file:
            fieldnames: list = ['name', 'email', 'phone']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            for contact in contacts:
                writer.writerow(contact)
        print(f"Contacts saved to CSV.")
    except FileNotFoundError:
        with open("contacts.csv", "w") as csv_file:
            fieldnames: list = ['name', 'email', 'phone']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(add_contact())

def delete_contacts(index):
    try:
        contacts.pop(index)
    except IndexError:
        print(f"Invalid Contact Number")

if __name__ == "__main__":
    main()