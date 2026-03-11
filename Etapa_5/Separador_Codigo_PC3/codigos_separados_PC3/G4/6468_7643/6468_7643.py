from math import *
l = float(input("Comprimento do lado do pentagono: "))

ap = l / 2 * tan(pi / 5)
p = 5 * l * ap / 2

print(round(p,2))