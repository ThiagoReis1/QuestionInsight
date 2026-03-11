#quantidade de pocoes em grama
x = int(input("Quantidade de pocoes: "))
from math import *
p1 = x * (((5 ** 0.5) - 1) / 4)
p2 = x * ((5 - 2 * (5 ** 0.5)) ** 0.5)
p3 = x * (5 * (5 - 2 * (5 ** 0.5)))
print(round(p1, 2))
print(round(p2, 2))
print(round(p3, 2)) 