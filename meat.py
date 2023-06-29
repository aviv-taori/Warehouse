from product import *

class Meat(Product):
    name = "Meat"

    def __init__(self, name, price, count):  # , barcode, expiry_date, manufacturer, supplier,kind):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return "Category:" + Meat.name + ", Name product: " + self.name + " The price: " + str(
            self.price) + " The count :" + str(self.count)

