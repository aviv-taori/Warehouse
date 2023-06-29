from management import *

class Product(ManagementSystem):
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count



    def update_price(self, new_price):
        self.price = new_price

    def print_product(self):
        print(self.name ,self.price)

