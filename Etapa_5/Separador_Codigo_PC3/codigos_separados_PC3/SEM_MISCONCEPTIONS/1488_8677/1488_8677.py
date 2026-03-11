minutos = int(input("insira o consumo do cliente: "))

if minutos > 0 and minutos <= 100:
	tarifa = (minutos * 1.20) + 1
elif minutos > 100 and minutos <= 200:
	tarifa = (minutos * 1.30) + 10
elif minutos > 200 and minutos <= 300:
	tarifa = (minutos * 1.40) + 20
else:
	tarifa = (minutos*1.50) + 25
	
print(round(tarifa, 2))