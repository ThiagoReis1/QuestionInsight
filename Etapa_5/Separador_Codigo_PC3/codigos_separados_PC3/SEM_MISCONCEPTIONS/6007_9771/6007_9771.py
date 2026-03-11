quant_espigas = int(input())

if quant_espigas >= 6:
	valor_total = quant_espigas * 1.50
	print(round( valor_total, 2))

else:
	valor_total = quant_espigas * 1.85
	print(round( valor_total, 2))