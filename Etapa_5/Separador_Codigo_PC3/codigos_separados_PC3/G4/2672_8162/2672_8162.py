from math import *
r = float(input("Raio: "))
n = int(input("Lados: "))
a = (1/2) * ((r * cos(pi/n))**2 * tan(pi/n))
print(round(a, 2))