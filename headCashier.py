from users import *

class HeadCashier(User):
    def __init__(self, username, password, id):
        super().__init__(self, username, password, id)
        self.usertype = "headCashier"



    def manage_inventory(self):
        # Inventory management logic here
        pass

