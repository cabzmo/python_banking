
class Person(object):

    def __init__(self, name, password, address = [None, None, None, None]):
        self.name = name
        self.password = password
        self.address = address
        # store parameters for personal details as attributes of the class

    def get_address(self):
        return self.address

    def update_name(self, name):
        self.name = name
        # TO IMPROVE: add a message or confirmation of name update
        
    def get_name(self):
        return self.name

    def print_details(self):
        print("Name %s:" %self.name)
        print("Address: %s" %self.address[0])
        print("         %s" %self.address[1])
        print("         %s" %self.address[2])
        print("         %s" %self.address[3])
        print(" ")
        # print each line of the address on a new line
        # using list indeces
        # TO IMPROVE: use a FOR loop to go through the indeces of the list

    def check_password(self, password):
        if self.password == password:
            return True
        return False
        # return a boolean value for whether the password passed as parameter
        # is the correct password

    def profile_settings_menu(self):
        #print the options you have
         print (" ")
         print ("Your Profile Settings Options Are:")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Update name")
         print ("2) Print details")
         print ("3) Back")
         print (" ")
         option = int(input ("Choose your option: "))
         return option

        
    def run_profile_options(self):
        loop = 1           
        while loop == 1:
            choice = self.profile_settings_menu()
            if choice == 1:
                name=input("\n Please enter new name\n: ")
                self.update_name(name)          
            elif choice == 2:                   
                self.print_details()
            elif choice == 3:
                loop = 0                     
