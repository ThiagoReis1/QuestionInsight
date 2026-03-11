from math import*
N = int(input("Digite o valor N:"))
soma = 0
i = 1
d = sqrt(i)
n = 4+3

while (i<=N):
	if (i%2==0):
		soma = soma - (d/(n))
	else:
		soma = soma + (d/(n))
	i = i+1
	d= sqrt(i)
	n = n+2
	
print(round(soma,9))
