from users import *

class Manager(User):
    def __init__(self, username, password, id, employers = None):
        super().__init__(self, username, password, id)
        self.username = username
        self.usertype = "manager"
        self.employers = []
        if employers == None:
            self.employers = []
        else:
            self.employers.append(employers)

    def __str__(self):
        return "name:" + self.username + ", password: " + str(self.password) + " type: " + self.usertype +" id: "+ str(self.id)  + " Number of em employers:" + str(len(self.employers))




    def add_employer(self,employer):
        if employer not in self.employers:
            self.employers.append(employer)
        else:
           print("The employer is on the team")

    def remove_employer(self, employer):
        if employer in self.employers:
            self.employers.remove(employer)
        else:
            print("The employer is not on the team")

    def print_manager_info(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"usertype: {self.usertype}")
        print(f"id: {self.id}")
        print("The employers")
        for employer in self.employers:
            print(f"Username: {employer.username}")
            print(f"Password: {employer.password}")
            print(f"usertype: {employer.usertype}")
            print(f"id: {employer.id}")
            print()

