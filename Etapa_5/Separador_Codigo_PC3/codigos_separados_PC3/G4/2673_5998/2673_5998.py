r = float(input("raio: "))
n = float(input("lado: "))

from math import *
l = 2 * r * sin(pi/n)
print(round(l, 2))