v0 = input("velocidade inicial: ")
d = input("distancia: ")
g = 9.8
from math import*
a = float((asin(d * g / v0 ** 2) * 90 / pi))
print(round(a, 2))