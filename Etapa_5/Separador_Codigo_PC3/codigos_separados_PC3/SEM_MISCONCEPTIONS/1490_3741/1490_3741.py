consumo = float(input("Digite: "))
Volume = float(input("Digite: "))
Tarifa = float(input("Digite: "))
Taxa = float(input("Digite: "))
Valor = Volume * Tarifa + Taxa

if (consumo == 0) or (consumo == 10):
	print(round(Valor, 2))