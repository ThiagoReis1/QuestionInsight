n = int(input("Digite o numero: "))
i = 0
soma = 0
sinal = 1
t = 0
while(i <= n):
	conta = sinal * (i) ** 2 / (4 + (2 * i - 1))
	soma = soma + conta
	sinal = - sinal
	i = i + 1
	t = t + 1
print(round(soma, 9))