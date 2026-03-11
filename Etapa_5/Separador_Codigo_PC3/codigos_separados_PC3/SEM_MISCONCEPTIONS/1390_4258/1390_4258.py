consumo = int(input("Consumo de minutos: "))

if(consumo <= 100):
	preco = 1.2*consumo
	print(round(preco, 2))

else:
	preco = 25 + 1.4*consumo
	print(round(preco, 2))