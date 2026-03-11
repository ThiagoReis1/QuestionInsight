minutos= float(input("Digite o valor de minutos:"))

if minutos <=100:
	tarifa = 1.20
	taxa = 1.0

elif minutos <=200:
	tarifa = 1.30
	taxa = 10.0
elif minutos <= 300:
	tarifa = 1.40
	taxa = 20.0
else:
		tarifa = 1.50
		taxa = 25.00
valor = minutos * tarifa + taxa
print(round(valor, 2))
		