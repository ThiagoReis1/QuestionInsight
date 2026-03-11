peso = float(input("informe o peso em gramas: "))

if peso <= 4999.9:
	c = 0.05 * peso
	print(round(c, 2))
else:
	b = 0.04*peso + 60
	print(round(b, 2))