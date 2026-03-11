from math import *

lado = float(input("Digite um valor: "))

apotema = lado / (2 * tan(pi / 12))

Area_12 = 6 * lado * apotema

print(round(Area_12, 2))