from math import*
b = float(input(""))
c = float(input(""))
a = radians(float(input("")))

val = sqrt(b**2 + c**2 - 2*b*c*cos(a))

print(round(val, 2))