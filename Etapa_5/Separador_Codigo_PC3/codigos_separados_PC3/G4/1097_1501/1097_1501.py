n = int(input("qual o valor: "))
n1 = n // 1000
n2 = n % 1000
X = ((n1 - n2) ** 2)
if (X == n):
	print(X, "atende a propriedade")
else:
	print(X)
