X = int(input("Digite quatro numeros: "))

num1 = X // 100
num2 = X % 100

if((num1 ** 2) + (num2 ** 2) == X):
	print(X, "atende a propriedade")
	
else:
	valor = (num1 ** 2) + (num2 ** 2)
	print(valor)