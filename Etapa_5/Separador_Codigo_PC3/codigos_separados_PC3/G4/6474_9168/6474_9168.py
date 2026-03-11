from math import *

l = float(input("Comprimento do lado do undecagono: "))

ap = l / (2*tan(pi/11))

Aun = (11*l*ap) / 2

print(round(Aun, 2))