b = float(input("b  "))
c = float(input("c  "))
d = float(input("d  "))
from math import *
f = radians(d)

a = sqrt(b**2 + c**2 - 2*b*c*cos(f))
print(round(a,2))