n = int(input("Digite um numero: "))
valor_inicial = 1
valor_final = n
i = 1
c = 2
while(i <= n):
	soma = soma + (-1) * i**3/(n * i + 3)
	i = i + 1
	n = n + 1
print(round(soma,8))