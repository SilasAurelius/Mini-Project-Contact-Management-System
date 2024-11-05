import re

def edit_contact():
    global contact_list
    pattern = r'^\+?\d{1,3}?[-.\s]?(\(?\d{1,4}?\)?[-.\s]?)?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    contact_name = input("Enter name of contact you want to edit: ").title()
    if contact_name in contact_list:
        contact_phone = input("Enter new phone number: ")
        if re.match(pattern, contact_phone):
            print(f"{contact_phone}: Valid phone number.")
        else:
            print(f"{contact_phone}: Not a valid phone number.")
        
        contact_email = input("Enter new email: ")
        contact_addition_info = input("Enter new additional information: ")
        
        contact_list[contact_name] = {
            "Phone number": contact_phone,
            "Email address": contact_email,
            "Additional information": contact_addition_info
        }
        print(f"{contact_name} has been updated.")
    else:
        print("Contact not found.")
