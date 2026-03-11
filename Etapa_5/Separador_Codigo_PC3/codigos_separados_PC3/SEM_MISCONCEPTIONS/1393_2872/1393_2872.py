peso = float(input("Informe o peso da encomenda: "))
if (peso > 4999.9):
	frete = (0.04*peso)+60
	print(float(round(frete,2)))
else:
	frete = (0.05*peso)
	print(float(round(frete,2)))
	