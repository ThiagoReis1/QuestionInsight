minutos = float(input())
if (minutos >= 0 and minutos <=100):
	tarifa = 1.2
	taxa = 1.0
elif (minutos >100 and minutos <=200):
	tarifa = 1.3
	taxa = 10.00
elif (minutos > 200 and minutos <=300):
	tarifa = 1.4
	taxa = 20.00
else:
	tarifa = 1.5
	taxa = 25.00
valor = minutos * tarifa + taxa
print(round(valor,2))