
#1
class ManagementSystem(object):
    def __init__(self):
        self.Warehouse = []
        self.users = []

    def show_Warehouse(self):
        return self.Warehouse

    def show_users(self):
        return self.users

    def add_users(self,user):
        self.users.append(user)

    def print_users_info(self):
        print(len(self.users))
        for user in self.users:
            print(f"Username: {user.username}")
            print(f"Password: {user.password}")
            print(f"usertype: {user.usertype}")
            print(f"id: {user.id}")
            print()


#2
class User():
    def __init__(self, username, usertype, password, id):
        self.username = username
        self.usertype = usertype
        self.password = password
        self.id = id

    def login(self, name, password):

        """
        If the username and password match you are logged in
        """
        if name == self.username and password == self.password:
            print("You are logged in")
        else:
            print("You are not logged in")

    def logout(self, name):
        if name == self.username:
            print("You are logout")

    def sign_up(self, new_username, new_password, new_usertype):
        self.username = new_username
        self.password = new_password
        self.usertype = new_usertype
        print("Sign up successful. You can now log in with your new credentials.")



    def login(self, name, password):

        """
        If the username and password match you are logged in
        """
        if name == self.username and password == self.password:
            print("You are logged in")
        else:
            print("You are not logged in")

    def logout(self, name):
        if name == self.username:
            print("You are logout")

    def sign_up(self, new_username, new_password,new_usertype):
        self.username = new_username
        self.password = new_password
        self.usertype = new_usertype
        print("Sign up successful. You can now log in with your new credential")


    def inventory(self):
        # Inventory logic here
        pass

    def orders(self):
        # Orders logic here
        pass


class HeadCashier(User):
    def __init__(self, username, id):
        super().__init__(username, id)

    def manage_cashier(self):
        # Cashier management logic here
        pass


class Manager(User):
    def __init__(self, username, id):
        super().__init__(username, id)

    def manage_staff(self):
        # Staff management logic here
        pass


class Storekeeper(User):
    def __init__(self, username, id):
        super().__init__(username, id)

    def manage_inventory(self):
        # Inventory management logic here
        pass

#3
class Warehouse(ManagementSystem):
    def __init__(self):
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

#4
class Product(ManagementSystem):
    def __init__(self, name, price, barcode, expiry_date, manufacturer, supplier,type):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.expiry_date = expiry_date
        self.manufacturer = manufacturer
        self.supplier = supplier
        self.type = type

    def search_product(self, product_name):
        Warehouse.search_product(product_name)

    def update_price(self, new_price):
        self.price = new_price

#5
class Milk(Product):
    def __init__(self, name, price, barcode, expiry_date, manufacturer, supplier, type):
        super().__init__(name, price, barcode, expiry_date, manufacturer, supplier,type)

class Meat(Product):
    def __init__(self, name, price, barcode, expiry_date, manufacturer, supplier, type):
        super().__init__(name, price, barcode, expiry_date, manufacturer, supplier,type)

class Bread(Product):
    def __init__(self, name, price, barcode, expiry_date, manufacturer, supplier, type):
        super().__init__(name, price, barcode, expiry_date, manufacturer, supplier, type)

class drinks(Product):
    def __init__(self, name, price, barcode, expiry_date, manufacturer, supplier, type):
        super().__init__(name, price, barcode, expiry_date, manufacturer, supplier, type)

class Housewares(Product):
    def __init__(self, name, price, barcode, manufacturer, supplier, type):
        super().__init__(name, price, barcode, manufacturer, supplier, type)

#6

class Account:
    def __init__(self):
        self.order_count = 0
        self.products_with_discount = []
        self.returned_products = []

    def calculate_stock(self):
        # Automatic stock calculation logic here
        pass

    def make_order(self):
        self.order_count += 1
        # Order creation logic here
        pass

print("Yes")


# # Example usage
# system_admin = ManagementSystem("admin", "admin", "password")
# system_admin.login()
#
# warehouse = Warehouse()
#
# milk = Milk("Milk", 2.99, "123456", "2023-06-30", "ABC Dairy", "XYZ Supplier", "2%")
# bread = Bread("Bread", 1.99, "654321", "2023-06-25", "ABC Bakery", "PQR Supplier", "Whole Wheat")
#
# warehouse.add_product(milk)
# warehouse.add_product(bread)
#
# warehouse.show_products()
#
# found_product = warehouse.search_product("Milk")
# # if found_product:
# #     found