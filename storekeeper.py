from users import *

class Storekeeper(User):
    def __init__(self, username, password, id):
        super().__init__(self, username, password, id)
        self.usertype = "storekeeper"




    def manage_inventory(self):
        # Inventory management logic here
        pass