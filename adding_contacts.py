
def add_contacts():
    import re
    pattern = r'^\+?\d{1,3}?[-.\s]?(\(?\d{1,4}?\)?[-.\s]?)?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
    contact_name = input("Enter full name: ").title()
    contact_phone = input("Enter phone number: ")
    if re.match(pattern, contact_phone):
        print(f"{contact_phone}: Valid phone number.")
    else:
        print(f"{contact_phone}: Not a valid phone number.")
    contact_email = input("Enter email: ")
    contact_addition_info = input("Enter additional information such as address or other information: ")
    
    
    contact_list[contact_name] = {
        "Phone number": contact_phone,
        "Email address": contact_email,
        "Additional information": contact_addition_info
    }
