from math import*

ang = eval(input(""))
k = int(input(""))

x = ang

p = 0
t = 0
w = 1

y = 1

while (t != k):
	p = 1 + (y*(x**w)/(w))
	t = t + 1
	w = w + 1
	y = y * (-1)

print(round(p, 10))