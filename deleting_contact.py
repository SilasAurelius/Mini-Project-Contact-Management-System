def delete_contact():
    global contact_list
    name = input("Enter the name of the contact you want to delete: ").title()
    if name in contact_list:
        del contact_list[name]
        print(f"{name} has been deleted successfully.")
    else:
        print("Contact name not found.")
