# Initialize contacts
contacts = [
    {'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}
]

def add_contact():
    name = input("Enter name: ")

    # Prevent duplicate contact
    for c in contacts:
        if c['name'] == name:
            print("Contact already exists")
            return

    phone = input("Enter phone: ")
    email = input("Enter email: ")

    # Validate phone
    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number")
        return

    # Validate email
    if '@' not in email or '.' not in email:
        print("Invalid email")
        return

    contacts.append({'name': name, 'phone': phone, 'email': email})
    print("Contact added successfully")

def display_contacts():
    for c in contacts:
        print(c)

def search_contact():
    name = input("Enter name to search: ")
    for c in contacts:
        if c['name'] == name:
            print(c)
            return
    print("Contact not found")

def update_contact():
    name = input("Enter name to update: ")
    for c in contacts:
        if c['name'] == name:
            c['phone'] = input("Enter new phone: ")
            c['email'] = input("Enter new email: ")
            print("Contact updated")
            return
    print("Contact not found")

def delete_contact():
    name = input("Enter name to delete: ")
    for c in contacts:
        if c['name'] == name:
            contacts.remove(c)
            print("Contact deleted")
            return
    print("Contact not found")

def sort_contacts():
    contacts.sort(key=lambda x: x['name'])
    print("Contacts sorted")

# Menu
while True:
    print("\n1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Sort Contacts")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        sort_contacts()
    elif choice == '7':
        break
    else:
        print("Invalid choice")