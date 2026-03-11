consumo = float(input(""))

if consumo < 10 :
	tarifa = 30 + 3*consumo
	
else:
	tarifa = 30 + 3.5*consumo
	
print(round(tarifa,2))