# #3
# from management import *
#
#
# # class HeadCashier(User):
# #     def __init__(self, username, id):
# #         super().__init__(username, id)
# #
# #     def manage_cashier(self):
# #         # Cashier management logic here
# #         pass
# #
# #
# # class Manager(User):
# #     def __init__(self, username, id):
# #         super().__init__(username, id)
# #
# #     def manage_staff(self):
# #         # Staff management logic here
# #         pass
# #
# #
# # class Storekeeper(User):
# #     def __init__(self, username, id):
# #         super().__init__(username, id)
# #
# #     def manage_inventory(self):
# #         # Inventory management logic here
# #         pass
#
# #3
#
# #4
#
#
# #5
#
#

#

# class Housewares(Product):
#     def __init__(self, name, price, barcode, manufacturer, supplier, type):
#         super().__init__(name, price, barcode, manufacturer, supplier, type)
#
# #6
#
# class Account:
#     def __init__(self):
#         self.order_count = 0
#         self.products_with_discount = []
#         self.returned_products = []
#
#     def calculate_stock(self):
#         # Automatic stock calculation logic here
#         pass
#
#     def make_order(self):
#         self.order_count += 1
#         # Order creation logic here
#         pass
#
#
#
#
# # # Example usage
# # system_admin = ManagementSystem("admin", "admin", "password")
# # system_admin.login()
# #
# # warehouse = Warehouse()
# #
# # milk = Milk("Milk", 2.99, "123456", "2023-06-30", "ABC Dairy", "XYZ Supplier", "2%")
# # bread = Bread("Bread", 1.99, "654321", "2023-06-25", "ABC Bakery", "PQR Supplier", "Whole Wheat")
# #
# # warehouse.add_product(milk)
# # warehouse.add_product(bread)
# #
# # warehouse.show_products()
# #
# # found_product = warehouse.search_product("Milk")
# # # if found_product:
# # #     found
