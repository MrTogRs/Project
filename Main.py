from Roots import Roots
from Roots import Discriminant
from Check import Check

a = input("введите a")
b = input("введите b")
c = input("введите c")

my_check = Check(a, b, c)

if my_check.check_values():
    my_dis = Discriminant(a, b, c)
    print(my_dis.get_discriminant())
    my_roots = Roots(a, b, my_dis.get_discriminant())
    print(my_roots.get_roots())
else:
    print("Введите числа")
