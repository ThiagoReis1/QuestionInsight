X = int(input("Digite um numero qualquer: "))

A1 = X // 100
Resto1 = X % 100

A2 = Resto1 // 10

A3 = Resto1 % 10


Soma = A1**3 + A2**3 + A3**3

if(Soma != X):
	print(Soma)
else:
	print(X, "atende a propriedade")

