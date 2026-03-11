numero_laranjas =  int(input("digite o numero: "))
if numero_laranjas >= 6:
	compras = (numero_laranjas * 0.75) - (numero_laranjas - 6) * 0.60
else:
	compras = numero_laranjas * 0.75
print(round(compras, 2))