X = int(input("Digite um numero: "))

x1 = X // 100
x2 = X % 100
y = (x1 + x2)**2

if (X == y):
    print(X, "atende a propriedade")
else:
	 print(y)