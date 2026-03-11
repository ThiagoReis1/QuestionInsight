from math import *
theta= radians(float(input("Angulo= ")))
d=float(input("Distancia= "))
g=9.8
V0=sqrt(d*(g/sin(2*theta)))
print(round(V0, 2))