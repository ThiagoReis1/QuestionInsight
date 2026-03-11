from math import *
lado = int(input("numero de lados: "))

apotema = lado / (2 * tan(pi/6))
area_Hex = (3 * lado * apotema)
print(round(area_Hex, 2))
# faça seu código aqui!