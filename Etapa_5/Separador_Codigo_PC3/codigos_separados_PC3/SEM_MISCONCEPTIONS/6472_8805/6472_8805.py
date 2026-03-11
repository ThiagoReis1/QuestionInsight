from math import *
lado = int(input("O comprimento do lado do eneagono: "))

x = tan(pi/9)
apotema = lado / (2 * x)
area_enag = (9 * lado * apotema) / 2

print(round(area_enag,2))