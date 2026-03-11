from math import sin, radians

angulo = radians(float(input()))
vel = float(input())
g = 9.8

d = vel**2*((sin(2*angulo))/g)
print(round(d, 2))