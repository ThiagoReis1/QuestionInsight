from math import*
n = int(input("Digite n: "))
p = 0
sinal= 1
i = 1
soma = 0

while(i <= n):
	p = p + sinal*sqrt(i)/(6 * 2 *i + 1)
	i = i + 1
	sinal = sinal

print(round(p,10))