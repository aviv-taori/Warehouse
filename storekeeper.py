from users import *
from warehouse import *

class Storekeeper(User):
    def __init__(self, username, password, id):
        super().__init__(self, username, password, id)
        self.usertype = "storekeeper"

    def storekeeper_search(self, product_name):
        if product_name in self.products:
            print("Name product: " + product_name.name, "The price: " + str(product_name.price),
                  "The count :" + str(product_name.count))
            print(self.products.index(product_name))