from math import *
lado = float(input("Digite o comprimento do lado do pentagono: "))
apotema = lado / (2 * tan(pi / 7))
area = (7 * lado * apotema) / 2
print(round(area, 2))