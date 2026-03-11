from math import *
a = eval(input(""))
k = int(input(""))
soma = 0
i = 0
sinal = 1

while (i < k):
	soma = soma + sinal * (a) ** (2 * i + 1) / factorial(2 * i + 1)
	i = i + 1
	sinal= -sinal

print(round(soma, 6))