def search_contact():
    global contact_list
    name = input("Enter the name of the contact you want to search: ").title()
    if name in contact_list:
        print(f"Contact found: {name} - {contact_list[name]}")
    else:
        print(f"Contact {name} not found.")
