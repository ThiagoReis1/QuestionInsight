from math import *
x = eval(input())
k = int(input())
y = 0
i = 0
z = 1
h = 0
while i < k:
	y = y + (z*(x ** i)/factorial(h))
	i = i + 1
	z = z*(-1)
	h = h + 2
print(round(y, 6))