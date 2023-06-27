from objects import *
from management import *
from users import *
from warehouse import *
from product import *
from milk import *
from meat import *
from bread import *
from drinks import *
from manager import *
from storekeeper import *
from headcashier import *




def main():
    yesh = ManagementSystem()
    a = Storekeeper("a", 123, 555)
    b = HeadCashier("b", 123, 555)
    c = Storekeeper("A", 11, 22)
    yesh.add_users(a)
    yesh.add_users(b)
    print(yesh.show_users())
    yesh.print_users_info()

    mang = Manager("BB", 111, 222, a)
    print()

    mang.add_employer(b)

    mang.print_manager_info()

    a1 = Warehouse("aaa")

    milk1 = Milk("3%", 22, 57)
    milk1.print_product()
    milk2 = Milk("5%", 22, 58)
    milk2.print_product()

    a1.add_product(milk1)
    a1.add_product(milk2)
    print()

    meat1 = Meat("red%", 22, 66)
    meat1.print_product()
    meat2 = Meat("reddd%", 22, 67)
    meat2.print_product()

    a1.add_product(meat1)
    a1.add_product(meat2)
    print()

    bread1 = Bread("white", 8, 77)
    bread1.print_product()
    bread2 = Bread("brown", 16, 78)
    bread2.print_product()

    a1.add_product(bread1)
    a1.add_product(bread2)
    print()

    drink1 = Drinks("coca", 9, 55)
    drink1.print_product()
    drink2 = Drinks("pepsi", 7, 56)
    drink2.print_product()

    a1.add_product(drink1)
    a1.add_product(drink2)
    print()

    a1.show_products()
    a1.delete_product(drink1)
    print()

    a1.show_products()
    print()

    a1.search_product(bread2)

    #a.storekeeper_search(bread2)




main()