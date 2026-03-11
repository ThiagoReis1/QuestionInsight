from math import *

lado = (float(input("o comprimento do lado do hexagono")))
apotema = lado / (2 * tan(pi/6))
areaHexagono = (3 * lado * apotema)
print(round(areaHexagono, 2))