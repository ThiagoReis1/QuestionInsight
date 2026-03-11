from math import *

#don't worry, be happy!

lado = float(input('Digite o lado do undecagono: '))

apotema = lado / (2 * tan(pi / 11))

area_undecagono = (11 * lado * apotema) / 2

print(round(area_undecagono, 2))
