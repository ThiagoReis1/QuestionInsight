import math

l = float(input())

p = l / (2*math.tan(math.pi/11))

a = (11 * l * p) / 2

print(round(a, 2))