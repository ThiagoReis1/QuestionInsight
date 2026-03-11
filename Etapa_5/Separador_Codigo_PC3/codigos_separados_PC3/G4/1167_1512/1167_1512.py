from math import*
n = int(input("n de termos: "))
soma = (-1 ** 3) / (7 + 1)
i = 1
x = 1
y = 1
e = 0

while (n >= i):
	if(i % 2 == 0):
		soma = soma + e
	else:
		soma = soma - e
	i = i + 1
	x = x + 1
	y = y + 2
	e = (x ** 2) / (7 + y)
print(round (soma, 11))