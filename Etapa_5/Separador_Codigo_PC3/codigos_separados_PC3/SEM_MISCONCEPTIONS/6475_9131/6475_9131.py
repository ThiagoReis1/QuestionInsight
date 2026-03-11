from math import *
lado = float(input("comprimento do lado: "))
apotema = lado / (2 * tan(pi/12))
area = 6 * lado * apotema
print(round(area, 2))
# faça seu código aqui!