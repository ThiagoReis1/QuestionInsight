from math import*
n = int(input("Digite o numero de casas de arredondamento: "))
r = 1
soma = 0
while (n > r):
	valor = 1 / factorial(n-1)
	soma = soma + valor
	n = n - 1
print (round(soma + 1.0, 8))