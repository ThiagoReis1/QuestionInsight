area = float(input("tamanho da area: "))

if (area <= 10000):
	valor = (area * 5)
	print(round(valor, 2))
else:
	aex = area - 10000
	valor = (area * 5) - (aex)
	print(round(valor , 2))