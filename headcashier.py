from users import *

class HeadCashier(User):
    def __init__(self, username, password, id):
        super().__init__(self, username, password, id)
        self.username = username
        self.usertype = "headCashier"

    # def headcashier_search(self, product_name):
    #     if product_name in self.products:
    #         print("Name product: " + product_name.name, "The price: " + str(product_name.price),
    #               "The count :" + str(product_name.count))
    #         print(self.products.index(product_name))

