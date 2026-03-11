pedido = input("Pedido (C ou E): ").upper()
quant = int(input("Quantidade de (C ou E): "))
suco = int(input("Quantidade suco: "))

if pedido.upper() == "C":
	valor = ((quant * 2.00) + (suco * 6.00))
	print(round(valor, 2))

else:
	valor = ((quant * 4.50) + (suco * 6.00))
	print(round(valor, 2))