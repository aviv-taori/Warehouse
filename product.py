from management import *

class Product(ManagementSystem):
    def __init__(self, name, price): #, barcode, expiry_date, manufacturer, supplier,kind):
        self.name = name
        self.price = price
        # self.barcode = barcode
        # self.expiry_date = expiry_date
        # self.manufacturer = manufacturer
        # self.supplier = supplier
        # self.kind = kind


    def update_price(self, new_price):
        self.price = new_price

    def print_product(self):
        print(self.name ,self.price)
