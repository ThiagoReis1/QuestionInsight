from math import*
n = int(input(""))
i = 1
sinal = -1
soma = 0
d = 8
while(i<=n):
	soma = soma + sinal*i**2/d
	i= i +1
	sinal = -sinal
	d = d + 2
print(round(soma,10))