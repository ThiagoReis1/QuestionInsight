pedido = input("Qual o pedido (C ou E): ")
quantidade = int(input("Qual a quantidade?: "))
quantidade_suco = int(input("Qual a quantidade de suco?: "))

Coxinha = 2.00
Esfirra = 4.50
Suco = 6.00

if (pedido == "C"):
	valor1 = Coxinha * quantidade
	valor2 = valor1 + (quantidade_suco * Suco)
	total = valor2
	print(round(total, 2))
	
else:
	valor1 = Esfirra * quantidade
	valor2 = valor1 + (quantidade_suco * Suco)
	total = valor2
	print(round(total, 2))

