from users import *

class Manager(User):
    def __init__(self, username, password, id, employees = None):
        super().__init__(self, username, password, id)
        self.username = username
        self.usertype = "manager"
        self.employees = []
        if employees == None:
            self.employees = []
        else:
            self.employees.append(employees)



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

        print( f"\nThe employees of {self.username}", )
        for employee in self.employees:
            print(f"Username: {employee.username}", f"Password: {employee.password}"
                  , f"usertype: {employee.usertype}", f"id: {employee.id}")

