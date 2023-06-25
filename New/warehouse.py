from management import *
class Warehouse:
    def __init__(self, name_warehouse):
        self.name_warehouse = name_warehouse
        self.products = []
        self.discarded_products = []
        self.sold_products = []

    def add_product(self, product):
        self.products.append(product)

    def delete_product(self, product):
        self.products.remove(product)

    def show_products(self):
        for product in self.products:
            print(product)

    def search_product(self, product_name):
        if product_name in self.products:
            print(product_name)
            print(self.products.index(product_name))

    # def update_product(self, product, new_price, new_info):
    #     product.price = new_price
    #     product.info = new_info
