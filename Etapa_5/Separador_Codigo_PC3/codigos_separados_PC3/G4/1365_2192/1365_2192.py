from math import *
a = float(input())
d = float(input())
rad = float(radians(a))
g = 9.8
v0 = round(float(((d*g)/sin(2*rad))**0.5), 2)
print(v0)


