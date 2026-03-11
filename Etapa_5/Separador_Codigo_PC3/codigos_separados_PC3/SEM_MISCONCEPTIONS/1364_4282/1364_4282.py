import math

v0 = float(input())
d = float(input())

angulo = math.asin(d * (9.8/(v0**2))) * 90/math.pi

print(round(angulo, 2))