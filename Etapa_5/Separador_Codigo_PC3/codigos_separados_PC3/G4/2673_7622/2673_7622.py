from math import *

r = float(input("insira o valor do raio: "))
n = int(input("insira o numero de lados: "))

l = 2 * r * sin(pi/n)

print(round(l, 2))