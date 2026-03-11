from math import*
n = int(input())
sinal = 1
den = 7
i = 1
soma = 0
while(n != 0):
	n = n - 1
	den = den + 2 
	sinal = - sinal
	i = i + 1
	soma = soma +(sinal * sqrt(i - 1) / den) 
	
print(round(soma,5))