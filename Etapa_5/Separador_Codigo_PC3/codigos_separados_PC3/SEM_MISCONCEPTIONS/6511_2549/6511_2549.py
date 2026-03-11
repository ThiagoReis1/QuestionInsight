entrada = input("Digite o tipo de entrada: ").upper()
quantidade = int(input("Quantidade desejada: "))

valor1 = 25.90 * quantidade
valor2 = valor1 - (valor1 * 0.1)
b = valor2

if (entrada == b):
	print(round(valor2, 2))
	
else:
	print(round(valor1, 2))