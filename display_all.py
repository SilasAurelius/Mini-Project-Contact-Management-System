def display_all_contacts(contact_list):
    if not contact_list:
        print("No contacts found.")
    else:
        for name, details in contact_list.items():
            print(f"{name}: {details}")
