from math import *
b = float(input(""))
c = float(input(""))
alfa = float(input(""))
a = sqrt(b**2 + c**2 - 2*b*c*cos(radians(alfa)))
print(round(a, 2))