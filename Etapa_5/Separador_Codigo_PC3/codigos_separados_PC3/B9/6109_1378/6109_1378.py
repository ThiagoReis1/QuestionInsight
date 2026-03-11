quant = int(input())

if quant > 0:
	if quant < 17.5:
		total = quant + 1.5
	elif quant >= 17.5 and quant < 35:
		total = quant + 2.3
	elif quant >= 35 and quant < 50:
		total = quant + 3.3
	else:
		total = quant + 4.7
print(round(total, 1))