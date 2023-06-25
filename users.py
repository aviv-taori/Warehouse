#2
from management import *


class User():
    def __init__(self, username, usertype, password, id):
        self.username = username
        self.usertype = usertype
        self.password = password
        self.id = id

    def login(self, name, password):

        """
        If the username and password match you are logged in
        """
        if name == self.username and password == self.password:
            print("You are logged in")
        else:
            print("You are not logged in")

    def logout(self, name):
        if name == self.username:
            print("You are logout")

    def sign_up(self, new_username, new_password, new_usertype):
        self.username = new_username
        self.password = new_password
        self.usertype = new_usertype
        print("Sign up successful. You can now log in with your new credentials.")



    def login(self, name, password):

        """
        If the username and password match you are logged in
        """
        if name == self.username and password == self.password:
            print("You are logged in")
        else:
            print("You are not logged in")

    def logout(self, name):
        if name == self.username:
            print("You are logout")

    def sign_up(self, new_username, new_password,new_usertype):
        self.username = new_username
        self.password = new_password
        self.usertype = new_usertype
        print("Sign up successful. You can now log in with your new credential")

#
#     def inventory(self):
#         # Inventory logic here
#         pass
#
#     def orders(self):
#         # Orders logic here
#         pass
#
#