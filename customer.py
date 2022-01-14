from person import Person

class Customer(Person):

    def __init__(self, name, password, address = [None, None, None, None]):
        super().__init__(name, password, address)
        # initialise a Person with personal details

    def open_account(self, account):
        self.account = account
        # self.account will contain an object of the class Account
        # which should be made before this function is called upon

    def get_account(self):
        return self.account
                            
    def print_details(self):
        super().print_details()                 # use method from Person class
        bal = self.account.get_balance()
        print('Account balance: %.2f' %bal)     # but add account balance
        print(" ")                              # at the end

							


