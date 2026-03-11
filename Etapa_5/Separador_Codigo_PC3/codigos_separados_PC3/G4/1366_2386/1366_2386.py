from math import *
g = 9.8
angulo = radians(float(input()))
vo = float(input())

d = (vo**2)*sin(2*angulo)/g

print(round(d, 2))