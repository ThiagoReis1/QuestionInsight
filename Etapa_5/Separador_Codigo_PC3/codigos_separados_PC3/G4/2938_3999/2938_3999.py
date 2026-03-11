from math import*
a=float(input())
b=float(input())
alfa=radians(float(input()))
c=sqrt(a**2+b**2-2*a*b*cos(alfa))
print(round(c,2))