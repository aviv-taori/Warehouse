from users import *

class Manager(User):
    def __init__(self, username, password, id, employers = None):
        super().__init__(self, username, password, id)
        self.username = username
        self.usertype = "manager"
        self.employees = []
        if employers == None:
            self.employees = []
        else:
            self.employees.append(employers)



    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
           print("The employer is on the team")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("The employer is not on the team")

    def print_manager_info(self):
        print(f"Username: {self.username}", f"Password: {self.password}"
              , f"usertype: {self.usertype}", f"id: {self.id}")

        print( "\nThe employees")
        for employee in self.employees:
            print(f"Username: {employee.username}", f"Password: {employee.password}"
                  , f"usertype: {employee.usertype}", f"id: {employee.id}")

