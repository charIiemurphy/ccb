from contact import Contact, ContactBook


contacts = ContactBook()

def create_contact():
    print('Let\'s create a contact!')
    # call our create contacts logic here
    print('Is this contact a business? y/n')
    choice = input('>> ')
    if choice == 'y':
        print('Okay. Creating a new business...')
        print('Enter the business name.')
        first_name = input('>> ')
        new_contact = Contact(first_name, True)
    elif choice == 'n':
        print('Okay. Creating a new person...')
        print('Enter a first name.')
        first_name = input('>> ')
        new_contact = Contact(first_name)
    # append new contact to the contacts array above
    contacts.add_contact(new_contact)
    print('Your contact has been created.')
    # back to main menu when done
    main_menu()


def print_contacts():
    print('Here are all of your contacts:')
    contacts.list_contacts()
    main_menu()


def quit_program():
    print('Goodbye!')


def main_menu():
    options = {
        1: 'Create a contact',
        2: 'List all contacts',
        0: 'Quit'
    }
    # maps each key to a method
    mapped_options = {
        1: create_contact,
        2: print_contacts,
        0: quit_program
    }
    print('What would you like to do?')
    for key in options.keys():
        print(str(key) + '. ' + options[key])
    # assuming good intent and valid input, no error handling
    user_input = input('>> ')
    # this calls the method corresponding to the integer choice
    mapped_options[int(user_input)]()
    
def start():
    print('Welcome to your contact book!')
    main_menu();

if __name__ == "__main__":
    start()
