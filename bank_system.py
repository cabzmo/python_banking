from customer import Customer
from admin import Admin
from account import Account

	
class BankSystem(object):
    def __init__(self):

        # initialise lists
        self.customers_list = []
        self.admins_list = []
        self.load_bank_data()

    def load_bank_data(self):
        
        # add test data into the program
        customer_1 = Customer("Adam", "1234", ["14", "Wilcot Street", "Bath", "B5 5RT"])
        account_no = 1234
        account_1 = Account(5000.00, account_no)
        customer_1.open_account(account_1)
        self.customers_list.append(customer_1)

        customer_2 = Customer("David", "password", ["60", "Holborn Viaduct", "London", "EC1A 2FD"])
        account_no+=1
        account_2 = Account(3200.00,account_no)
        customer_2.open_account(account_2)
        self.customers_list.append(customer_2)


        customer_3 = Customer("Alice", "MoonLight", ["5", "Cardigan Street", "Birmingham", "B4 7BD"])
        account_no+=1
        account_3 = Account(18000.00,account_no)
        customer_3.open_account(account_3)
        self.customers_list.append(customer_3)


        customer_4 = Customer("Ali", "150A",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"])
        account_no+=1
        account_4 = Account(40.00,account_no)
        customer_4.open_account(account_4)
        self.customers_list.append(customer_4)


        admin_1 = Admin("Julian", "1441", True, ["12", "London Road", "Birmingham", "B95 7TT"])
        self.admins_list.append(admin_1)

        admin_2 = Admin("Eva", "2222", False, ["47", "Mars Street", "Newcastle", "NE12 6TZ"])
        self.admins_list.append(admin_2)


    def customer_login(self):
        #STEP A.1

        name = input ("\nPlease input customer name: ")

        found_customer = self.search_customers_by_name(name)
        if found_customer != None:
            password = input ("\nPlease input customer password: ")
            if (found_customer.check_password(password) == True):
                self.run_customer_options(found_customer)
            else:
                return("You have entered a wrong password")
        
        #pass
        
    def search_customers_by_name(self, customer_name):
        #STEP A.2

        found_customer = None
        for a in self.customers_list:
            name = a.get_name()
            if name == customer_name:
                found_customer = a
                break
        if found_customer == None:
            print("\nThe customer %s does not exist! Try again...\n" %customer_name)

        return found_customer
        
        #pass


    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Customer login")
        print ("3) Quit Python Bank System")
        print (" ")
        option = input ("Choose your option: ")
        return option

    def run_main_option(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            try:
                choice = int(choice)

                if choice == 1:
                    msg = self.admin_login()
                    if msg != None:
                        print(msg)
                elif choice == 2:
                    msg = self.customer_login()
                    if msg != None:
                        print(msg)
                elif choice == 3:
                    loop = 0
                elif choice > 3 or choice < 1:
                    print("\nPlease enter an integer between 1 and 3")    

            except:
                print("\nPlease enter an integer between 1 and 3")

        print ("Thank-You for stopping by the bank!")


    def transferMoney(self, customer):

##      customer.get_account(), receiver_name, receiver_account_no, amount
        sender_account = customer.get_account()
        receiver_name = input("\nTo whom are you sending money: ")
        found_receiver = self.search_customers_by_name(receiver_name)
        if found_receiver != None:
            receiver_account = found_receiver.get_account()
            receiver_account_no = input("\nType in the account number: ")
            try:
                receiver_account_no = int(receiver_account_no)
                if  int(receiver_account_no) == int(receiver_account.get_account_no()):
                    try:
                        amount = int(input("\nType in the amount you wish to transfer: "))
                        if amount < 0:
                            print("\nSorry, you have entered an invalid amount ... Please try again")
                            self.run_customer_options(customer)
                        elif amount > sender_account.balance:
                            print("\nSorry, not enough balance to proceed this transaction")
                            self.run_customer_options(customer)
                        else:
                            sender_account.balance = sender_account.balance - amount
                            receiver_account.balance = receiver_account.balance + amount
                            print("\n\nJust transfered", amount, "to Ali. THANKS\n")
                            sender_account.print_balance()
                    except:
                        print("\nPlease enter integers ONLY for amount")
                else:
                    print("\nThat account number is not linked to an account in the given name ... Please try again")
                    self.run_customer_options(customer)
            except:
                print("\nPlease enter integers ONLY for account number")
                self.run_customer_options(customer)
            #print("Sorry there was an error during the process ... Please contact a system administrator")
                
        #pass

        #find receiving account using receiver_name and receiver_account_no


    def customer_menu(self, customer_name):
        #print the options you have
         print (" ")
         print ("Welcome %s : Your transaction options are:" %customer_name)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Other account operations")
         print ("3) profile settings")
         print ("4) Sign out")
         print (" ")
         option = int(input ("Choose your option: "))
         return option

    
    def run_customer_options(self, customer):
                    
        account = customer.get_account()            
        loop = 1
        while loop == 1:
            choice = self.customer_menu(customer.get_name())
            if choice == 1:

                self.transferMoney(customer)
                
            elif choice == 2:
                account.run_account_options()
            elif choice == 3:
                customer.run_profile_options()
            elif choice == 4:
                loop = 0
        print ("Exit account operations")

                
    def admin_login(self):
        # STEP A.3

        name = input ("\nPlease input admin name: ")
        
        
        found_admin = self.search_admin_by_name(name)
        if found_admin != None:
            password = input ("\nPlease input admin password: ")
            if (found_admin.check_password(password) == True):
                self.run_admin_options(found_admin)
            else:
                return("You have entered a wrong password")
            
        
        #pass


    def search_admin_by_name(self, admin_name):
        # STEP A.4

        found_admin = None
        for a in self.admins_list:
            name = a.get_name()
            if name == admin_name:
                found_admin = a
                break
        if found_admin == None:
            print("\nThe admin %s does not exist! Try again...\n" %admin_name)

        return found_admin
    
        #pass


    def admin_menu(self, admin_name):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s : Avilable options are:" %admin_name)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations")
         print ("3) Customer profile settings")
         print ("4) Admin profile settings")
         print ("5) Delete customer")
         print ("6) Print all customers detail")
         print ("7) Sign out")
         print (" ")
         option = int(input ("Choose your option: "))
         return option

    def admin_transferMoney(self, admin_name):
        
        sender_name = input("enter the sender's name: ")

        found_sender = self.search_customers_by_name(sender_name)
        if found_sender == None:
            pass
        else:
            
            sender_account_no = input("enter the sender's account number: ")
        
            sender_account = found_sender.get_account()
            if int(sender_account.get_account_no()) == int(sender_account_no):
                print("\nBalance is ... ", int(sender_account.balance))
    
                
                receiver_name = input("enter the receiver's name: ")
                receiver_account_no = input("enter the receiver's account number: ")

                found_receiver = self.search_customers_by_name(receiver_name)
                if found_receiver == None:
                    pass
                else:
                    receiver_account = found_receiver.get_account()
                    if int(receiver_account.get_account_no()) == int(receiver_account_no):
                        amount = input("enter the amount of money you wish to transfer: ")
                        if float(amount) >= float(sender_account.get_balance()):
                            print("You do not have enough money in your account to complete this transfer. Sorry ...")
                            self.admin_menu(admin_name)
                        else:
                            sender_account.balance = sender_account.balance - float(amount)
                            receiver_account.balance = receiver_account.balance + float(amount)
                            print("EXCHANGE SUCCESSFUL!!!")
                            self.admin_menu(admin_name)
                    else:
                        print("\nAn account with that account number does not exist ...")
                        self.admin_menu(admin_name)
            else:
                print("\nAn account with that account number does not exist ...")
                self.admin_menu(admin_name)
    
    def run_admin_options(self, admin):
                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin.get_name())
            if choice == 1:
                self.admin_transferMoney(admin.get_name())
            elif choice == 2:
                #STEP A.5

                customer_name = input("\nPlease input customer name :\n")
                customer = self.search_customers_by_name(customer_name)
                if customer != None:
                    account = customer.get_account()
                    if account != None:
                        account.run_account_options()
                
            elif choice == 3:
                #STEP A.6

                customer_name = input("\nPlease input customer name :\n")
                customer = self.search_customers_by_name(customer_name)
                if customer != None:
                    customer.run_profile_options()
                
            elif choice == 4:
                #STEP A.7

                admin.run_profile_options()
                
            elif choice == 5:
                #STEP A.8

                admin_name = self.search_admin_by_name(admin.name)
                if admin_name.has_full_admin_right() == True:
                    customer_name = input("\nPlease input customer name you want to delete :\n")
                    customer = self.search_customers_by_name(customer_name)
                    if customer != None:
                        self.customers_list.remove(customer)
                        print()
                        print(customer_name, "has been deleted from the system")
                        print("------------------------")
                        print()
                        self.print_all_accounts_details()
                else:
                    print("\nOnly administrators with full admin rights can remove a customer from the bank system!\n")

                
                #pass
            elif choice == 6:
                #STEP A.9

                self.print_all_accounts_details()

                
                #pass
            elif choice == 7:
                loop = 0
        print ("Exit account operations")


    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.customers_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")

        



app = BankSystem()
app.run_main_option()
