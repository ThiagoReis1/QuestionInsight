from math import *
a = float(input("distancia a: "))
b = float(input("distancia b: "))
y = float(input("angulo y: "))
d = cos(radians(y))
c = ((a**2) + (b**2) - (2 * a * b * d))**0.5
print(round(c, 2))