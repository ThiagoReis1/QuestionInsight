x = float(input("Digite o numero real: "))
k = int(input("Digite a qtd de termos: "))
i = 0
soma = 0
while (i < k):
	soma = soma + ( (i + 1) / (2 * (i + 1) * x))
	i = i + 1
print(round(soma,10))
	