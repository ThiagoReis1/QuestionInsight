from math import *
a = float(input("Observador e a arvore 1: "))
b = float(input("Observador e a arvore 2: "))
ang = radians(float(input("Ang entre a e b: ")))
c = sqrt(a**2+b**2-2*a*b*cos(ang))
print (round(c, 2))