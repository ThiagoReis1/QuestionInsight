from math import *

n = int(input("Insira um numero inteiro: "))

soma = sqrt(1)/(4+3)
i = 1
x = 1
y = 3
e = 0

while (i <= n):
	if (i % 2 == 0):
		soma = soma - e
	else:
		soma = soma + e
	x = x + 1
	y = y + 2
	i = i + 1
	e = sqrt(x)/(4 + y)
print (round (soma, 9))