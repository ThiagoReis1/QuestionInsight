area_fertilizada = float(input("Digite o valor da area fertilizada: "))

if (area_fertilizada <= 10000):
	valor_total = area_fertilizada * 5.00
	print(round(valor_total, 2))
	
else:
	valor_total = (10000 * 5) + 4.00 * (area_fertilizada - 10000)
	print(round(valor_total, 2))
	