from math import*
n = int(input(""))
i = 1
x = 1
y = 3
e = 0
soma = - sqrt(1)/(6 + y)

while(i <= n):
	if(i % 2 == 0):
		soma = soma + e
	else:
		soma = soma - e
	i = i + 1
	x = x + 1
	y = y + 2
	e = sqrt(x) / (6 + y)
print( round(soma, 5))