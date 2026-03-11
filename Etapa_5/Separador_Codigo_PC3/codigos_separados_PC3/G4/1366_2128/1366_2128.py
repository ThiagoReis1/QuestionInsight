from math import *
angulo=float(input())
vel=float(input())
g=9.8
angulo=radians(angulo)
d=vel**2*sin(2*angulo)/g
print(round(d,2))