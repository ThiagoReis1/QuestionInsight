from math import *
r = float(input("Raio: "))
l = int(input("Lados: "))

A = ((1/2) * ((r*cos(pi/l))**2 * tan(pi/l)))
print(round(A,2))