from math import *

raio = float(input("Valor do Raio: "))
n = float(input("Numero de lados n: "))

L = 2*raio*sin(pi/n)

print(round(L, 2))

