itens = input("L ou P: ")
quant_p_l = int(input("quant_p_l: "))
quant_refri = int(input("quantR: "))


if itens == "P":
	print(quant_p_l * 4.50 + quant_refri * 3.00)
else:
	print(quant_p_l * 6.00 + quant_refri * 3.00)
