numero = int(input())

x = numero // 100
y = numero % 100

valor_da_soma_das_partes = (x+y) ** 2

if (numero == (x+y) ** 2):
	print(numero, "atende a propriedade")
else:
	print(valor_da_soma_das_partes)