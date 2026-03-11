import math as m

r = float(input())
n = int(input())

pi = m.pi
l = 2 * r * m.sin(pi/n)

print(round(l, 2))