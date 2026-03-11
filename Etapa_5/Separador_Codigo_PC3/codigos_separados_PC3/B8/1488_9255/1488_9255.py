minutos = int(input("Insira o consumo em minutos: "))

if (minutos >= 0) and (minutos <= 100):
	valor = (minutos * 1.20) + 1
	print(round(valor, 2))
elif (minutos > 100) and (minutos <= 200):
	valor = (minutos * 1.30) + 10
	print(round(valor, 2))
elif (minutos > 200) and (minutos <= 300):
	valor = (minutos * 1.40) + 20
	print(round(valor, 2))
elif minutos > 300:
	valor = (minutos * 1.50) + 25
	print(round(valor, 2))