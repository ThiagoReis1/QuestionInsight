from math import*
a=float(input('a='))
b=float(input('b='))
x=radians(float(input('x=')))
c=sqrt(a**2+b**2-2*(a*b*cos(x)))
print(round(c,2))