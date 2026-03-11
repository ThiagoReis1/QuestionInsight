from math import *

lado = float(input("Digite o comprimento do lado do dodecagono: "))

a = lado / (2 * tan(pi/12))

area = 6 * lado * a

print(round(area,2))