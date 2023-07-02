from product import *

class Drinks(Product):
    name = "Drinks"

    def __init__(self, name, price, count):
        super().__init__(name, price, count)

    def __str__(self):
        return "Category:" + Drinks.name + ", Name product: " + self.name + " The price: " + str(
            self.price) + " The count :" + str(self.count)
