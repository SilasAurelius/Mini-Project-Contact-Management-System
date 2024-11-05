def import_contacts():
    global contact_list
    filename = input("Enter the filename to import contacts: ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(" | ")
                name = parts[0].split(": ")[0]
                phone = parts[0].split(": ")[1]
                email = parts[1]
                additional_info = parts[2]
                
                contact_list[name] = {
                    "Phone number": phone,
                    "Email address": email,
                    "Additional information": additional_info
                }
        print(f"Contacts imported from {filename} successfully.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
