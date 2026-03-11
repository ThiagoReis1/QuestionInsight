from math import *
a = float(input("distancia a: "))
b = float(input("distancia b: "))
y = radians(float(input("angulo: ")))
c = sqrt(a**2 + b**2 - 2*a*b * cos(y))
print(round(c,2))