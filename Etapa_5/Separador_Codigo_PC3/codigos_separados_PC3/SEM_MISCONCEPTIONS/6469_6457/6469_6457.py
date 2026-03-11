from math import *

lado = int(input("Digite o comprimento do lado do hexagono: "))

apotema = lado / (2 * tan(pi/6))

area = 3 * lado * apotema

print(float(round(area, 2)))