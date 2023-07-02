from management import *
class Warehouse:
    def __init__(self, name_warehouse):
        self.name_warehouse = name_warehouse
        self.products = []
        self.discarded_products = []
        self.sold_products = []

    #products
    def add_product(self, product):
        self.products.append(product)

    def delete_product(self, product):
        self.products.remove(product)

    def show_products(self):
        for product in self.products:
            print("Name product: " + product.name, "The price: " + str(product.price),
                  "The count :" + str(product.count))



    def search_product(self, product_name):
        print("The index for product:", self.products.index(product_name))
        if product_name in self.products:
            print("Name product: " + product_name.name, "The price: " + str(product_name.price),
                  "The count :" + str(product_name.count))

     # discarded_products
    def add_product_discarded(self, product):
        self.discarded_products.append(product)

    def delete_product_discarded(self, product):
        self.discarded_products.remove(product)

    def show_products_discarded(self):
        for product in self.discarded_products:
            print("Name product: " + product.name, "The price: " + str(product.price),
                  "The count :" + str(product.count))

    # sold_products
    def add_product_sold(self, product):
        self.sold_products.append(product)

    def delete_product_sold(self, product):
        self.sold_products.remove(product)

    def show_products_sold(self):
        for product in self.sold_products:
            print("Name product: " + product.name, "The price: " + str(product.price),
                  "The count :" + str(product.count))



    
