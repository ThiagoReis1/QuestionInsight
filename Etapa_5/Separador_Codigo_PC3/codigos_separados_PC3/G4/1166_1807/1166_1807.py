from math import *
n = int(input("Insira um número inteiro:"))
i = 0
m = 1
l = 1
sinal = 1
soma = 0
while(n > i):
	s = ((m** (0.5))/(6 + l))* sinal
	i = i + 1
	m = m + 1
	l = l + 2
	soma = soma + s
	sinal = sinal * (-1)
print(round(soma,10))	