from math import *
r = float(input("Raio: "))
n = int(input("Numero de lados: "))
l = 2*r*sin(pi/n)
print(round(l,2))
