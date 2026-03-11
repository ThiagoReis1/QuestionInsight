import math

r = float(input())
l = int(input())
pie = math.pi

A = (1/2)*((r*math.cos(pie/l))**2)*math.tan(pie/l)
print(round(A,2))