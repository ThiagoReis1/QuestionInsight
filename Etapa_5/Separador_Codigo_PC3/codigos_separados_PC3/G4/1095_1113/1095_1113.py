X = int(input("Digite um numero: "))
x1 = X // 10000
resto_x1 = X % 10000

y = (x1 + resto_x1) ** 2

if( X == y ):
	print(X, "atende a propriedade")
else:
	print(y)