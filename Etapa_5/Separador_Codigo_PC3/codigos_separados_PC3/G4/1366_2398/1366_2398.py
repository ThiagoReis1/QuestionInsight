from math import*
angulo = radians(float(input()))
v0 = float(input())
g = 9.8
d = (v0**2)*sin(2*angulo)/g
print(round(d, 2))