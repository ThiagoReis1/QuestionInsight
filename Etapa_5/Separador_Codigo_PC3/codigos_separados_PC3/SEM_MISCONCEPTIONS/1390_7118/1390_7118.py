consumo = float(input(""))

if consumo <= 100:
	tarifa = 1.20 * consumo 
	
else: 
	tarifa = 25 + (1.40 * consumo)
	
print(round(tarifa, 2))