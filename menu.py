# empty when first initialized
# global scope, can be accessed within all methods
contacts = []

def create_contact():
    print('Let\'s create a contact!')
    # call our create contacts logic here
    # append new contact to the contacts array above
    # e.g. contacts.append(new_contact)
    print('Your contact has been created.')
    main_menu()


def list_contacts():
    print('Here are all of your contacts:')
    # we should call our list contact method here
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
        2: list_contacts,
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


start()
    
