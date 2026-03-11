from math import *

# faça seu código aqui!

lado = float(input("Digite os lado: "))
opotema = lado / (2 * tan(pi/9))
area_eneagono = (9 * lado * opotema) / 2

print(round(area_eneagono,2))