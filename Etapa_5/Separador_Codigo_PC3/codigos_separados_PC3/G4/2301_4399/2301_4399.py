import math

b = float(input())
c = float(input())
angulo = math.radians(float(input()))

a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(angulo))

print(round(a, 2))