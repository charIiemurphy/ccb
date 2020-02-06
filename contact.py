
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

class ContactBook:
    def __init__(self):
        self.book = []

    def __readContacts(self):
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

    def __writeContacts(self, contacts):
        """write the input strings 'contacts' to a file"""
        filepath = 'contacts-export.csv'
        fptr = open(filepath, 'w')

        fptr.write(result)
        fptr.close()
    
    def exportAll(self):
        """Export all contacts to a file"""
        __writeContacts(__readContacts())

        