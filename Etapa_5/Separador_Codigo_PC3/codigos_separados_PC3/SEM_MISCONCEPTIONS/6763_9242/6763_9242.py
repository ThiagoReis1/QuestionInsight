tempo = float(input("tempo reservado: "))

if tempo < 2.00:
	taxa = 1.25
elif tempo == 2.00:
	taxa = 2.25
else:
	taxa = 3.25
	
tarifa = 5.00 + taxa
print(round(tarifa, 2))