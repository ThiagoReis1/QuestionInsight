pedido = input("L se for lanche ou P se for pizza: ").upper()
qtd = int(input("Quantidade de lanches ou pizzas: "))
qtd_ref = int(input("Quantidade de refrigerantes: "))


if	pedido == "L":
	print(6.00 * qtd + 3.00 * qtd_ref)
else:
	print(4.50 * qtd + 3.00 * qtd_ref)