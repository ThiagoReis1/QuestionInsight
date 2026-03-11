peso = float(input("Peso da encomenda:" ))
if (peso <= 4999.9):
	x = peso * 0.05
	print(round(x,2))
else:
	x = peso * 0.04 + 60
	print(round(x,2))
						 