valor = float(input("valor consumido"))
if (0 < valor <= 300):
	total = (((valor*10)/100)+valor)
	print(total)
if (0< valor > 300):
	total2 = (((valor*6)/100)+valor)
	print(total2)