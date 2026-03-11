consumo = float(input("Minutos de um cliente: "))

if consumo <= 100: 
	tarifa = 1.20
	valor = consumo * tarifa 
	print(round(valor,2))

if consumo > 100: 
	taxa = 25.0 
	tarifa = 1.40 
	valor = (consumo * tarifa) + taxa 
	print(round(valor,2))
