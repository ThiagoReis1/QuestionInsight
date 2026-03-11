from math import *
# faça seu código aqui!
lado = float (input("digite o lado: "))
#area eneagono
apotema = lado / (2 * tan (pi / 9))
area_Eneagono = 9 * lado * apotema / 2
#apotema

print(round(area_Eneagono, 2))