
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
