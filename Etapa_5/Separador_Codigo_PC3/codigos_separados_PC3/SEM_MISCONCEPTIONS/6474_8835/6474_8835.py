from math import *
lado = float(input("Valor do lado:"))
apotema = lado/ (2 * tan(pi/11))
AU = 11 * lado * apotema/ 2

print(round(AU,2))