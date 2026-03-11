from math import *
Ax = (float(eval(input())))
k = int(input())
n = 0
cont = 0
j = 1
v = 0
e = 0
while cont < k:
	e = e + (Ax**(v)/factorial(n))*j
	n += 2
	cont += 1
	v += 1
	j *= -1
print(round(e,6))