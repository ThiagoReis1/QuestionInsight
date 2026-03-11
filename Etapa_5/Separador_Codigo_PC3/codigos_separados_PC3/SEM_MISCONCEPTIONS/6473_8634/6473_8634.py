from math import *

# faça seu código aqui!
lado = float(input("Comprimento do lado do decagono: "))
apotema = float(lado/(2 * tan(pi/10)))

area = 5 * lado * apotema

print(round(area, 2))