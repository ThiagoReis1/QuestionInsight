from math import *
b=float(input("Valor do labo B:"))
c=float(input("Valor do lado C:"))
ang=radians(float(input("Valor do angulo alfa:")))

d=sqrt(b**2 + c**2 - 2*b*c*cos(ang))

print(round(d,2))