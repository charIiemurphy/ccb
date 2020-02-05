'''
A spike determining how to sort and list the set of contacts
on the console.
'''

from contact import Contact

def list_contacts(contacts):
    ''' 
    Print contacts to console in alphabetical order based
    on last name.

    Arguments
    ---------
    contacts: list of Contact objects
        The list of contacts currently stored.

    Returns
    -------
    nothing. Prints contacts to console.
    '''
    # Sort the list of Contacts alphabetically by last name
    contacts.sort(key = lambda contact: contact.last_name)

    # Print the contacts to the console
    print('Listing current contacts:\n')

    for contact in contacts:
        print(
            f'First Name: {contact.first_name} '
            f'Last Name: {contact.last_name}\n'
        )

def main():

    # Create three example contacts
    alice = Contact(first_name = 'Alice')
    alice.last_name = 'Apples'

    bob = Contact(first_name = 'Bob')
    bob.last_name = 'Burger'

    conor = Contact(first_name = 'Conor')
    conor.last_name = 'Contact'

    # Store in list with last name out of alphabetical order
    contact_list = [bob, conor, alice]

    # Use the list contact function
    list_contacts(contact_list)


if __name__ == "__main__":
    main()