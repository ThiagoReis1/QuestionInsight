x = int(input("digite o numero:"))

valor = x // 10000
valor2 = x % 10000
y = (valor + valor2)**2

if(x == y):
	print(x, "atende a propriedade")
else:
	print(y)

