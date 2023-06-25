#`
from objects import *

class ManagementSystem(object):
    def __init__(self):
        self.warehouses = []
        self.users = []

    def show_Warehouses(self):
        return len(self.warehouses)

    def show_users(self):
        return len(self.users)

    def add_users(self,user):
        self.users.append(user)

    def add_warehouses(self,warehouse):
        self.warehouses.append(warehouse)

    def print_users_info(self):
        print(len(self.users))
        for user in self.users:
            print(f"Username: {user.username}")
            print(f"Password: {user.password}")
            print(f"usertype: {user.usertype}")
            print(f"id: {user.id}")
            print()

    def print_warehouse_info(self):
        print(len(self.warehouses))
        # for ware in self.warehouse:
        #     print(f"warehousname: {warehouse.name_warehouse}")

        print()

