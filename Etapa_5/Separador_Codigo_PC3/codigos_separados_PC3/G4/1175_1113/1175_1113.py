from math import*
N = int(input("Digite o numero de termos da serie: "))

i = 1
soma = 0
sinal = -1
while(i <= N):
	soma = soma + (sinal * sqrt(i)/ (6 + (2*i + 1)))
	sinal = - sinal
	i = i + 1
print(round(soma, 5))