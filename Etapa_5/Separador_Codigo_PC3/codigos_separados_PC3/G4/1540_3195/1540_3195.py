from math import *
x = eval(input())
k = int(input())
v = 0
m = 0
l = 0
while (v < k):
	m = m  - ((-1)**(v+1))*((x**v)/(factorial(l)))
	l = l + 2
	v = v + 1
print(round(m, 6))