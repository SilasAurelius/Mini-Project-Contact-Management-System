from adding_contacts import *
from search_contacts import *
from deleting_contact import *
from editing_contacts import *
from display_all import *
from exporting_contacts import *
from importing_contacts import *

contact_list = {}
pattern = r'^\+?\d{1,3}?[-.\s]?(\(?\d{1,4}?\)?[-.\s]?)?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'

print("Welcome to the Contact Management System!")

while True:
    print("Menu:")
    print("1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit")
    
    try:
        user_choice = int(input("Enter selection: "))
    except ValueError:
        print("Please enter your choice as a number.")
        continue
    except Exception as e:
        print(f"Unknown Error: {e}")
        continue

    if user_choice == 1:
        add_contacts()
    elif user_choice == 2:
        edit_contact()
    elif user_choice == 3:
        delete_contact()
    elif user_choice == 4:
        search_contact()
    elif user_choice == 5:
        display_all_contacts()
    elif user_choice == 6:
        export_contacts()
    elif user_choice == 7:
        import_contacts()
    elif user_choice == 8:
        print("Thank you for using the Contact Management System.\nGoodbye!")
        break
