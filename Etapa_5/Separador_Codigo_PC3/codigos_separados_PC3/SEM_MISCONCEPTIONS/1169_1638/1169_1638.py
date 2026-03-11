from math import *
n = int(input("digite o valor de n:"))
i =1
soma = 0
sinal =1
while(i<=n):
	conta = -sinal * sqrt(i) / (9 + (2*i -1))
	soma = soma + conta
	sinal = - sinal
	i = i + 1
print(round(soma,6))
										 