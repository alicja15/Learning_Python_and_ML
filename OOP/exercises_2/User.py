class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, name):
        if len(name) >= 3:
            self.__username = name
        else:
            print("Username too short")
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email_name):
        if '@' in email_name:
            self.__email =  email_name
        else:
            print("Invalid email")


u1 = User("Al", "al@domena.pl")  # Username too short
u2 = User("Alicja", "alicja.pl") # Invalid email

