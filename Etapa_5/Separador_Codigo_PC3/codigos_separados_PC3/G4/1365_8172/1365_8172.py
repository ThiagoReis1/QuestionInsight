from math import sin, radians, sqrt

ang = float(input())
d = float(input())

Vi = sqrt(d*(9.8/sin(2*radians(ang))))

print(round(Vi,2))