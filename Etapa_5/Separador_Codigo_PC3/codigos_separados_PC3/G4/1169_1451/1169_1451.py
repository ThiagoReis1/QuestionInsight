from math import*
n = int(input("Digite o numero: "))
i = 0
sinal = 1
soma = 0
while(i < n):
	soma = soma - sinal * (sqrt(i + 1)) / (9 + (2*i + 1))
	sinal = -sinal
	i = i + 1
print(round(soma,6))
