# Letícia Filardi - 21601147
# Avaliação 2

n = int (input ("Digite um número:"))

n1 = n // 1000
n2 = n % 1000

X = ((n1 + n2) ** 2)

if (X == n):
	print(X, "atende a propriedade")
else:
	print(X)