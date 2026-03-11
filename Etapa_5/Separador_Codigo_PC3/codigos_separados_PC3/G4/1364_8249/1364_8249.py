from math import*

vi = float(input())
d = float(input())

ang = asin (d * 9.8 / vi ** 2) * (90 / pi)

print(round(ang, 2))