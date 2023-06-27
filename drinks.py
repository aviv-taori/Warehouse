from product import *

class Drinks(Product):
    name = "Drinks"
    def __init__(self, name, price,count):  # , barcode, expiry_date, manufacturer, supplier,kind):
        self.name = name
        self.price = price
        self.count = count

    def print_product(self):
        print("Category:",Drinks.name,",Name product: " + self.name,"The price: " + str(self.price),"The count :" + str(self.count))
