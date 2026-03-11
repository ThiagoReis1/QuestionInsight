from math import*
n = int(input("Digite um numero:"))
i = 1
soma = 0
sinal = 1
while(i <= n):
	soma = soma + sinal * (sqrt (i) / (4 + (2*i + 1)))
	sinal = - sinal
	i = i + 1
print(round(soma, 9))