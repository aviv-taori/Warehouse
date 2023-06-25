from warehouse import ManagementSystem
from warehouse import User


def main():
    yesh = ManagementSystem()
    a = User("a","b",123,555)
    b = User("b", "b", 123, 555)
    yesh.add_users(a)
    yesh.add_users(b)
    print(len(yesh.show_users()))
    yesh.print_users_info()

main()
print(123)
