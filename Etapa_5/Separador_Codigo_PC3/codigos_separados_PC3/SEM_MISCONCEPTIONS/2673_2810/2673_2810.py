from math import *
r = float(input("digite um valor: "))
n_lados = int(input("digite um valor: "))

L = 2 * r * sin(pi / n_lados)

print(round(L, 2))