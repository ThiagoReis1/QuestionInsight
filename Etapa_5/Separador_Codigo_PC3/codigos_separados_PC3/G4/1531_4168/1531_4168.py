from math import*
x = eval(input("angulo em radianos:"))
k = int(input("quantidade de termos:"))
i = 0
p = 0
soma = 0
sinal = 1
while ( i < k):
	soma = soma + ((x**p) / factorial(p))*(sinal)
	i = i + 1
	p = p + 2
	i = i + 2
	sinal = sinal * (-1)
print(round(soma,10))