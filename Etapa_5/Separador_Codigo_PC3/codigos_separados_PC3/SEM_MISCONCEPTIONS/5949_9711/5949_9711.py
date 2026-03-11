pedido = input("digite se B ou C?")
quant = int(input("digite a quantidade de fatias: "))
quant2 = int(input("digite a quantidade de cappuccinos: "))

if pedido.upper() == "B":
	valor = (3.00 * quant) + (quant2 * 5.50)
	print(round(valor, 2))
else:
	valor2 = (6.00 * quant) + (quant2 * 5.50)
	print(round(valor2, 2))