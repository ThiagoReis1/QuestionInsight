import math

b = float(input())
c = float(input())
alfa = float(input())

a = (b*b + c*c - 2*b*c*math.cos(math.radians(alfa)))**0.5

print(round(a, 2))