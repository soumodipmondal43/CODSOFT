contacts = []  # List to store contacts


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address (optional): ")
    address = input("Enter Address (optional): ")
    new_contact = Contact(name, phone, email, address)
    contacts.append(new_contact)
    print("Contact Added Successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    print("-" * 50)
    print("| Name          | Phone Number     |")
    print("-" * 50)
    for contact in contacts:
        print(f"| {contact.name:15} | {contact.phone:15} |")
    print("-" * 50)


def search_contact():
    search_term = input("Enter search term (name or phone number): ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact.name.lower() or search_term in contact.phone.lower()]
    if not found_contacts:
        print("Contact not found!")
        return
    print("-" * 50)
    print("| Name          | Phone Number     |")
    print("-" * 50)
    for contact in found_contacts:
        print(f"| {contact.name:15} | {contact.phone:15} |")
    print("-" * 50)


def update_contact():
    view_contacts()
    name_to_update = input("Enter name of contact to update: ")
    found_contact = None
    for contact in contacts:
        if contact.name.lower() == name_to_update.lower():
            found_contact = contact
            break
    if not found_contact:
        print("Contact not found!")
        return
    new_name = input("Enter new name (leave blank to keep old): ") or found_contact.name
    new_phone = input("Enter new phone number (leave blank to keep old): ") or found_contact.phone
    new_email = input("Enter new email address (leave blank to keep old): ") or found_contact.email
    new_address = input("Enter new address (leave blank to keep old): ") or found_contact.address
    found_contact.name = new_name
    found_contact.phone = new_phone
    found_contact.email = new_email
    found_contact.address = new_address
    print("Contact Updated Successfully!")


def delete_contact():
    view_contacts()
    name_to_delete = input("Enter name of contact to delete: ")
    found_contact = None
    for i, contact in enumerate(contacts):
        if contact.name.lower() == name_to_delete.lower():
            found_contact = i
            break
    if not found_contact:
        print("Contact not found!")
        return
    confirm = input(f"Are you sure you want to delete {contacts[found_contact].name}? (y/n): ")
    if confirm.lower() == 'y':
        del contacts[found_contact]
        print("Contact Deleted Successfully!")


def main_menu():
    print("\nContact Management System")
    print("-" * 30)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice


while True:
    choice = main_menu()
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting...")
        break
