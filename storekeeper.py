from users import *


class Storekeeper(User):
    def __init__(self, username, password, id):
        super().__init__(self, username, password, id)
        self.username = username
        self.username = username
        self.usertype = "storekeeper"





    def search_storekeeper(self,warehouse, product_name):
        warehouse.search_product(product_name)



