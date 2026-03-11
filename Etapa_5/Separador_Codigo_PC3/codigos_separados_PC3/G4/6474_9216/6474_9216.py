from math import *

c = float (input("Digite o comprimento do lado do undecagono: "))

x = pi / 11
a = tan (x)
apotema = c / (2 * a)

area = (11 * c * apotema) / 2

print (round(area,2))