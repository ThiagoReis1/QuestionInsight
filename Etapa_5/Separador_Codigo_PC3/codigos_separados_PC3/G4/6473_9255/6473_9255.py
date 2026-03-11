from math import *
lado = float(input("Insira o lado: "))
b = (pi/10)
a = tan(b)
ap = lado / (2 * a)
area = 5 * lado * ap
print(round(area, 2))