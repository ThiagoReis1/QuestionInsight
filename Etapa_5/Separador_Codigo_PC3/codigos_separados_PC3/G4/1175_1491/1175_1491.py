N = int(input("Insira um numero inteiro: "))
i = 0
m = 1
l = 3
sinal = 1
soma = 0
while( N > i):
	s = (((-1) * m ** (0.5)) /(6 + l)) * sinal
	i = i + 1
	m = m + 1
	l = l + 2
	soma = soma + s
	sinal = sinal * (-1)
print(round(soma,5))