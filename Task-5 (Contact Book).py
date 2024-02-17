class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

def add_contact(contact_book, max_contacts):
    if len(contact_book) < max_contacts:
        name = input("Enter the name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        contact_book.append(Contact(name, phone, email, address))
        print("Contact created successfully.")
    else:
        print("Contact Book directory is full. Can't add more contacts.")

def search_contact(contact_book):
    if contact_book:
        search_name = input("Enter the name you want to search for: ")
        found = False
        for contact in contact_book:
            if contact.name == search_name:
                print("Name:", contact.name)
                print("Phone Number:", contact.phone)
                print("Email:", contact.email)
                print("Address:", contact.address)
                found = True
                break
        if not found:
            print("Contact not found")
    else:
        print("Contact Book directory is empty. Create a contact first.")

def display_contacts(contact_book):
    if contact_book:
        print("Contact Book Entries")
        for contact in contact_book:
            print("-----------------------------")
            print("Name :", contact.name)
            print("Phone number :", contact.phone)
            print("Email :", contact.email)
            print("Address :", contact.address)
            print("------------------------------")
    else:
        print("Contact Book directory is empty. Add a contact first.")

def edit_contact(contact_book):
    if contact_book:
        search_name = input("Enter the name of the contact you want to edit: ")
        found = False
        for contact in contact_book:
            if contact.name == search_name:
                print("Editing contact:", contact.name)
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email address: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully.")
                found = True
                break
        if not found:
            print("Contact not found")
    else:
        print("Contact Book directory is empty. Create a contact first.")

def delete_contact(contact_book):
    if contact_book:
        search_name = input("Enter the name of the contact you want to delete: ")
        found = False
        for contact in contact_book:
            if contact.name == search_name:
                contact_book.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break
        if not found:
            print("Contact not found")
    else:
        print("Contact Book directory is empty. No contact to delete.")

def main():
    max_contacts = 100  # Number of Maximum Contacts
    contact_book = []

    while True:
        print("\n CONTACT BOOK DIRECTORY")
        print("1. Add a Contact.")
        print("2. Search for a Contact.")
        print("3. Display all Contacts.")
        print("4. Edit a Contact.")
        print("5. Delete a Contact.")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contact_book, max_contacts)
        elif choice == '2':
            search_contact(contact_book)
        elif choice == '3':
            display_contacts(contact_book)
        elif choice == '4':
            edit_contact(contact_book)
        elif choice == '5':
            delete_contact(contact_book)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
