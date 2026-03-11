from math import *
a = float(input("raio"))
p = float(input("preco do fertilizante"))
A = (pi * a ** 2)
custo = (round(p * A,2))
print(custo)
