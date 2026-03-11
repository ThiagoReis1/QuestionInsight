from math import *

a = radians(float(input("angulo = ")))
d = float(input("distancia ="))

v = ((d*9.8)/sin(2*a))**(1/2)

print(round(v, 2))