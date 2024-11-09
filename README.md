#
I wrote multiple functions as separate modules to import to have clean, organized code. This allowed me to write and debug my code quickly.

main.py is the core of the program. Initially, I import all my functions and regex to define global values. 
The user is greeted and given options for adding contacts. A dictionary builds key-value pairs matching name, phone, email, and additional notes. 
#
Try/Except blocks are used for error handling such as the user typing letters instead of a number for the menu choice.

adding_contacts.py is where the add_contacts(contact_list, pattern) function is defined. I used contact_list and pattern as the parameters because the list and the defined regex pattern are needed here and in editing_contacts.py. This allows the user to input the contact list details and validate a phone number.
#
delete_contact(contact_list) deletes a contact completely. 
#
display_all_contacts(contact_list) calls to display the dictionary of contact names, phone numbers, email, and additional details.
#
export_contacts(contact_list) and import_contacts(contact_list) will either export a text file or import one to the folder path you choose. I use with open( , 'r') as file because that lets me read the file and safely close it.
#
search_contact(contact_list) prompts the user to enter the name of the contact. The function checks if the name is in the list. If not, an error message is produced. 
#
Whenever the user is done, they can select 8 from the menu to see a Goodbye message. This then breaks the loop and ends the program.
