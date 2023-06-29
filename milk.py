from product import *

class Milk(Product):
    name = "Milk"

    def __init__(self, name, price, count):
        super().__init__(name, price, count)


    def __str__(self):
        return "Category:" + Milk.name + ", Name product: " + self.name + " The price: " + str(
            self.price) + " The count :" + str(self.count)

