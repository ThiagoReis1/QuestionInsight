from math import sin, sqrt, radians

d = float(input())
a = radians(float(input()))
g = 9,8

v0 = sqrt(d*(g)/sin(2*a))

print(round(v0,2))