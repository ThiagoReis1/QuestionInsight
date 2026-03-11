from math import *

# faça seu código aqui!
compr = float(input('Comprimento do lado do decagono:'))

apotema = (compr) / (2 * tan( pi / 10 ))

area = 5 * compr * apotema

print(round(area, 2))