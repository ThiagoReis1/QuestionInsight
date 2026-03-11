c = float(input("Consumo: "))
if (c <= 150):
	tarifa = 0.60 * c + 5
else: 
	tarifa = 0.75 * c + 16
print(round(tarifa, 2))