from warehouse import *
from milk import *
from meat import *
from bread import *
from drinks import *
from manager import *
from storekeeper import *
from headcashier import *



def main():
    osher = ManagementSystem()

    Noach = Storekeeper("Noach", 121212, 44444)
    Moach = Storekeeper("Moach", 232323, 55555)
    Rosh = HeadCashier("Rosh", 343434, 66666)

    osher.add_users(Noach)
    osher.add_users(Moach)
    osher.add_users(Rosh)

    print(osher.show_number_users())
    osher.print_users_info()

    Meny = Manager("Meny", 123456, 98765, Noach)
    print()

    Meny.add_employee(Moach)
    Meny.add_employee(Rosh)

    Meny.print_manager_info()

    a1 = Warehouse("osher")

    print("\nProduct")

    milk1 = Milk("3%", 7, 57)
    print(milk1)
    milk2 = Milk("5%", 8, 58)
    print(milk2)

    a1.add_product(milk1)
    a1.add_product(milk2)
    print()

    meat1 = Meat("red", 40, 66)
    print(meat1)
    meat2 = Meat("red_red", 50, 67)
    print(meat2)

    a1.add_product(meat1)
    a1.add_product(meat2)
    print()

    bread1 = Bread("white", 8, 77)
    print(bread1)
    bread2 = Bread("brown", 16, 78)
    print(bread2)

    a1.add_product(bread1)
    a1.add_product(bread2)
    print()

    drink1 = Drinks("coca", 9, 55)
    print(drink1)
    drink2 = Drinks("pepsi", 7, 56)
    print(drink2)

    a1.add_product(drink1)
    a1.add_product(drink2)
    print()

    a1.show_products()
    a1.delete_product(drink1)
    print()

    a1.show_products()
    print()

    
    Moach.search_storekeeper(a1,bread1)
    print()

    Rosh.headcashier_show(a1)




main()
