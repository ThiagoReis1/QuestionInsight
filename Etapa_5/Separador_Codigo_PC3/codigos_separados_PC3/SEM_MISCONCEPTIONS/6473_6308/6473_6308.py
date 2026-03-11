from math import *

comprimentoLado = int(input())

apotema = comprimentoLado / (2 * tan((pi/10)))

area = 5 * comprimentoLado * apotema

print(round(area,2 ))