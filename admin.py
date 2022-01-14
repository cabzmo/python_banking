
from person import Person

class Admin(Person):
    
    def __init__(self, name, password, full_rights, address = [None, None, None, None]):
        super().__init__(name, password, address)
        self.full_admin_rights = full_rights
        # initialise a Person with personal details
        # but add boolean variable 'full_admin_rights'

    def has_full_admin_right(self):
        return self.full_admin_rights
        # return boolean value of 'full_admin_rights'

