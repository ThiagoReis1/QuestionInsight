from math import *

# faça seu código aqui!
#entradas
lado = float(input("lado do decagono: "))

apotema = lado / (2 * tan( pi / 10))

area = 5 * lado * apotema

print(round(area, 2))