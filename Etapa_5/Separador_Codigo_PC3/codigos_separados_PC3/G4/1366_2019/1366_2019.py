from math import *
a = float(input("angulo: "))
b = float(input("velocidade: "))
g=9.8
d= (b**2 * sin(2 * radians(a))/g)
print (round (d,2))