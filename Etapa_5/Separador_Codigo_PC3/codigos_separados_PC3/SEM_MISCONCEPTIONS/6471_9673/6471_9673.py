from math import *

x = float(input("Qual o comprimento do lado: "))

apotema = x / (2 * tan(pi / 8))
areaO = 4 * x * apotema

print(round(areaO, 2))