consumo = float(input("Insira o valor do consumo (em m3):\n"))
tarifa = 0

if (consumo < 10):
	tarifa = 3 * consumo
else:
	if (consumo >= 10):
		tarifa = 3.5 * consumo
		
taxa_total = tarifa + 30
print(taxa_total)
	