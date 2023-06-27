from objects import *
from management import *
from users import *
from warehouse import *
from product import *
from milk import *
from meat import *
from bread import *
from drinks import *



def main():
    yesh = ManagementSystem()
    a = User("a","b",123,555)
    b = User("b", "b", 123, 555)
    yesh.add_users(a)
    yesh.add_users(b)
    print(yesh.show_users())
    yesh.print_users_info()
    a1 = Warehouse("aaa")

    milk1 = Milk("3%",22,57)
    milk1.print_product()
    milk2 = Milk("5%", 22,58)
    milk2.print_product()
    print()

    meat1 = Meat("red%", 22,66)
    meat1.print_product()
    meat2 = Meat("reddd%", 22,67)
    meat2.print_product()
    print()

    bread1 = Bread("white", 8,77)
    bread1.print_product()
    bread2 = Bread("brown", 16,78)
    bread2.print_product()
    print()

    drink1 = Drinks("coca", 9,55)
    drink1.print_product()
    drink2 = Drinks("pepsi", 7,56)
    drink2.print_product()
    print()

main()
