from math import *

angulo=radians(float(input()))
d= float(input())
a=9.8/sin(2*angulo)
v=(d*a)**0.5

print(round(v,2))