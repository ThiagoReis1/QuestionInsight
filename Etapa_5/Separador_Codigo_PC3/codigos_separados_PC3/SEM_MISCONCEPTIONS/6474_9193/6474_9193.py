from math import *

lado = float(input("Digite o lado do undecagono: "))

apotema = lado / (2 * tan(pi/11))
area = (11 * lado * apotema) / 2

print(round(area, 2))