from math import *

a = radians(float(input("angulo = ")))
v0 = float(input("velocidade inicial = "))
g = 9.8
d = (v0**2) * ( (sin( (2 * a) ) / g) )

print(round(d, 2))
