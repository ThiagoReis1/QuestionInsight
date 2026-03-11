vo = float(input("velocidade inicial: "))
d = float(input("distancia: "))
a = 30
g = 9.8
from math import *
a = asin(d * (g / vo ** 2)) * 90 / pi
print(round(a, 2))