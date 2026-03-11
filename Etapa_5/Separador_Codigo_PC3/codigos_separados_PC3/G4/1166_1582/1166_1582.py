# gabriel siza  de oliveira brandão - 21601146
# av.4

n = int(input("digite o numero"))
i = 0
m = 1
l = 1
sinal = 1
soma = 0

while (n>i):
	s = ((1)* m**(0.5)) / (6 + l) * sinal
	i = i + 1
	m = m + 1
	l = l + 2
	soma = soma + s
	sinal = sinal * (-1)
print(round(soma,10))