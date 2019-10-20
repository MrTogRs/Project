from Dis import Dis
from Roots import Roots


my_dis = Dis(3.2, -7.8, 1)
print(my_dis.discriminant_count())
my_roots = Roots(3.2, -7.8, 1, my_dis.discriminant_count())
print(my_roots.roots_count())

