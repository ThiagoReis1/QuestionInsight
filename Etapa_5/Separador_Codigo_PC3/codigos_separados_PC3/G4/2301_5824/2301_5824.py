from math import *
b=float(input("b: "))
c= float(input("c: "))
angulo=radians(float(input("angulo: ")))
a=((b**2)+(c**2)-2*b*c*cos(angulo))**0.5
print(round(a,2))