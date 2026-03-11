from math import *
lado = float(input("lado"))

apotema = lado / (2 * tan(pi/6))
area = 3 * lado * apotema
# faça seu código aqui!
print(round(area,2))