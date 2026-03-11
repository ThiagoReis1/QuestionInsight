quant = int(input("Digite a quantidade de combustivel comum:"))

if quant < 17.5:
	total = quant + 1.5
	print(round(total,2))
elif quant >= 17.5 and quant < 35:
	total = quant + 2.3
	print(round(total,2))
elif quant >= 35 and quant < 50:
	total = quant + 3.3
	print(round(total,2))
elif quant >= 50:
	total = quant + 4.7
	print(round(total,2))