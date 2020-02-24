import os 

class Contact:
    def __init__(self, first_name, business=False):
        self.business = business
        self.first_name = first_name
        self.last_name = None
        self.email = None
        self.phone_number = None
        self.notes = None
        self.social_media = { 'instagram': None, 'facebook': None }
        if not business:
            self.birthday = None

    def __str__(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.first_name}'

    # Prints all information about a particular contact
    def print_self(self):
        print('First Name: ' + self.first_name)
        if self.last_name: print('Last Name: ' + self.last_name)
        if self.business: print('Business: ' + str(self.business))
        if self.email: print('Email: ' + self.email)
        if self.phone_number: print('Phone Number: ' + self.phone_number)
        if self.notes: print('Notes: ' + self.notes)
        if self.social_media['instagram']: print('Instagram: ' + self.social_media['instagram'])
        if self.social_media['facebook']: print('Facebook ' + self.social_media['facebook'])


class ContactBook:
    def __init__(self):
        self.book = []
        self.file = 'contacts-export.csv'
        if os.path.isfile(self.file):
            self.book = self.__read()

    def __read(self):
        """Returns all contacts in the contact book as a formatted string"""

        # start with headers
        result = 'first_name,last_name,business,email,phone,notes,instagram,facebook\n'
        delim = ',' # separates touchpoints into columns
        for contact in self.book:
            
            # for each contact, add each available touchpoint
            result += contact.first_name + delim

            if contact.last_name:
                result += contact.last_name
            result += delim

            result += str(contact.business).lower() + delim

            if contact.email:
                result += contact.email
            result += delim

            if contact.phone_number:
                result += contact.phone_number
            result += delim

            if contact.notes:
                result += '"' + contact.notes + '"'
            result += delim

            if contact.social_media['instagram']:
                result += contact.social_media['instagram']
            result += delim

            if contact.social_media['facebook']:
                result += contact.social_media['facebook']
            result += '\n'

        return result

    def __write(self, contacts):
        """write the input strings 'contacts' to a file"""
        fptr = open(self.file, 'w')

        fptr.write(self.__read())
        fptr.close()
    
    def add_contact(self, new_contact):
        self.book.append(new_contact)

    def list_contacts(self):
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
        self.book.sort(key = lambda contact: contact.first_name)

        # Print the contacts to the console
        print('Listing current contacts:')
        for contact in self.book:
            print(contact)

    def export_all(self):
        """Export all contacts to a file"""
        self.__write(self.__read())

    def search_by_last_name(self, name):
        """Find contacts with a particular last name"""
        # isolate to contacts with a stored last name
        contacts = [x for x in self.book if x.last_name]

        # special case for empty list
        num_contacts = len(contacts)
        if num_contacts == 0:
            print('No contact in the book has a stored last name')
            return # not found

        # sort by last name alphabetically
        contacts.sort(key=lambda x: x.last_name)

        # binary search
        start = 0
        end = num_contacts
        while start <= end:
            # mid is index of contact to check
            mid = ((end - start) // 2) + start

            # compare input name to current mid of book
            if name > contacts[mid].last_name:
                start = mid + 1
                continue # restart loop
            elif name < contacts[mid].last_name:
                end = mid - 1
                continue # restart loop

            # last name found - find first instance in book
            if mid != 0:
                while (contacts[mid-1].last_name == name):
                    mid -= 1
                    if mid == 0:
                        break

            # print all contacts with found last name
            while (contacts[mid].last_name == name):
                print(contacts[mid])
                mid += 1
                if mid == num_contacts:
                    break

            return # found

        print('No contact with the last name ' + name + ' found')
        return # not found

    # CAN DELETE returns contact at index number "number"
    def returnContactInfo(self, number):
        return self.book[number]
