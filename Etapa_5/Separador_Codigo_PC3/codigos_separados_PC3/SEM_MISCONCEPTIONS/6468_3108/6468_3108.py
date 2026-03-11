from math import *
lado = float(input("Comprimento do lado do pentagono: "))
apotema = lado / (2* tan(pi/5))
areaPentagono = (5 * lado * apotema) / 2
print(round(areaPentagono, 2))