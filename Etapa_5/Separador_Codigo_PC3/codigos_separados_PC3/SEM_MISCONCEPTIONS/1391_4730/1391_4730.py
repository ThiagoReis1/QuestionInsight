kwh=float(input("consumo de energia"))

if(kwh<=150):
	tarifa=(0.60*kwh) + 5
	
else:
	tarifa=(0.75*kwh)+16
print(round(tarifa,2))