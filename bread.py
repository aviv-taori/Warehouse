from product import *

class Bread(Product):
    def __init__(self, name, price):  # , barcode, expiry_date, manufacturer, supplier,kind):
        self.name = name
        self.price = price

    def print_product(self):
        print(self.name, self.price)

