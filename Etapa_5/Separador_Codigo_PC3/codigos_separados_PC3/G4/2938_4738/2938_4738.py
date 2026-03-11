from math import*
a=float(input())
b=float(input())
d=radians(float(input()))

c=sqrt(a**2+b**2-2*a*b*cos(d))
print(round(c,2))