quant = int(input("informe a quantidade de tomates comprados: "))

if quant < 4:
	total = quant * 0.75
else:
	total = quant * 0.55
	
print(round(total, 2))
