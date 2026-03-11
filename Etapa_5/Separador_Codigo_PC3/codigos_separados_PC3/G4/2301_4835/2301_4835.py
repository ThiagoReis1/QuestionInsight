from math import*
b = float(input())
c = float(input())
ang = float(input())
angu= radians(ang)
a = (b**2+c**2-2*b*c*cos(angu))**0.5
print(round(a,2))