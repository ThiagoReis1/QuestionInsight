from math import *

r = float(input("valor do raio"))
l = int(input("numero de lados n"))

L = 2 * r * sin(pi/l)

print(round(L, 2))