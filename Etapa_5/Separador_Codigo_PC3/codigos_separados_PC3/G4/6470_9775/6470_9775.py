from math import *

# faça seu código aqui!
lado = float(input("Comprimento do lado: "))

apo = lado / (2 * tan(pi*1/7))

area = 7 * lado * apo / 2

print(round(area, 2))