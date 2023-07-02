from product import *

class Meat(Product):
    name = "Meat"

    def __init__(self, name, price, count):
        super().__init__(name, price, count)

    def __str__(self):
        return "Category:" + Meat.name + ", Name product: " + self.name + " The price: " + str(
            self.price) + " The count :" + str(self.count)

