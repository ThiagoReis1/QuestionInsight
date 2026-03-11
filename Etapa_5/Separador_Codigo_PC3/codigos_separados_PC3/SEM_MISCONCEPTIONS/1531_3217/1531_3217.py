from math import *
x = eval(input())
k = int(input())
v = 1
m = 0
l = 1
while(v<=k):
	m = m + ((-1)**(v+1))*((x**l)/(factorial(l)))
	l = l + 1
	v = v + 2
print(round(m, 10))








troco alma por habilidade de passar nessa subeta