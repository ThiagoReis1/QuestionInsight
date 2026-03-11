pedido = input("Digite L para Lanche e P para pizza: ")
quant = int(input("Quantidade de lanche ou pizza: "))
refri = int(input("Quantos refrigerantes? "))
if pedido.upper() == "L":
	PF = (6.00 * quant) + (3.00 * refri)
	print(round(PF, 2))
else:
	PF = (4.50*quant) + (3.00 * refri)
	print(round(PF, 2))