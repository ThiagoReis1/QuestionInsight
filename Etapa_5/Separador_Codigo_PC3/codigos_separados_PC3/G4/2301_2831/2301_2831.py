from math import*

b=float(input())
c=float(input())
ang=radians(float(input()))

a=((b**2)+(c**2)-(2*b*c*cos(ang)))**(0.5)

print(round(a,2))