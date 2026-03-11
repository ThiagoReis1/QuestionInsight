peso = float(input("o peso da encomenda "))

if(peso>=5000.0):
	taxa=60.00
	valor=peso*0.04+taxa
	print(round(valor, 2))
else:
	valor=peso*0.05
	print(round(valor, 2))