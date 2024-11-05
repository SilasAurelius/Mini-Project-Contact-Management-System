def export_contacts():
    global contact_list
    filename = input("Enter the filename to export contacts: ")
    with open(filename, 'w') as file:
        for name, details in contact_list.items():
            file.write(f"{name}: {details['Phone number']} | {details['Email address']} | {details['Additional information']}\n")
    print(f"Contacts exported to {filename} successfully.")
