from math import *

lados = float(input("comprimento: "))

apotema = lados / (2 * tan (pi/12))
area = 6 * lados * apotema

print(round(area, 2))