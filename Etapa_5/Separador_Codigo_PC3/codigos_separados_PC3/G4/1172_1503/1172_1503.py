n = int(input("insira um numero inteiro:"))
i = 0
m = 1
l = 3
sinal = 1
soma = 0
while (n > i):
	s = m**0.5/(4 + l)*sinal
	sinal = -1*sinal
	i = 1 +i
	l = l + 2
	m = m + 1
	soma = soma + s
print(round(soma,9))
	