from math import*
b=float(input("b"))
c=float(input("c:"))
g=float(input("angulo"))
a=sqrt((b**2)+(c**2)-2*b*c*cos(radians(g)))
print(round(a,2))
