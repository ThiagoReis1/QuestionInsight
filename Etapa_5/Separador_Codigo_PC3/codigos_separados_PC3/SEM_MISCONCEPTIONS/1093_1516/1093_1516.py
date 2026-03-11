numero = int(input("digite o numero:"))

x = (numero // 100)**2 + (numero % 100) **2

if(numero == x):
	print(x, "atende a propriedade")
else:
	print(x)