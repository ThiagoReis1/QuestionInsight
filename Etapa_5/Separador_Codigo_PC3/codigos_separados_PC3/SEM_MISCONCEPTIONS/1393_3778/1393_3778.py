peso = float(input())

if peso <= 4999.9:
	cons = 0.05
else:
	cons = 0.04

	frete = cons * peso + 60
	print(round(frete, 2))