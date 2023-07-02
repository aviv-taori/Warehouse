from users import *

class HeadCashier(User):
    def __init__(self, username, password, id):
        super().__init__(self, username, password, id)
        self.username = username
        self.usertype = "headCashier"

    def headcashier_show(self, warehouse):
        warehouse.show_products()

