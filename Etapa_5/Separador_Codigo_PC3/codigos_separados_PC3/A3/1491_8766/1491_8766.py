peso = float(input("Digite o valor do frete:"))


if (peso >= 0) and  (peso <= 5000):
	tarifa = 0.03
	taxa = 20
	valor = (peso * 0.03) + 20
	print(valor)
elif (peso > 5001) and (peso <= 6000):
	tarifa = 0.04
	taxa = 25
	valor = (peso * 0.04) + 25
	print(valor)
elif (peso > 6001) and (peso <= 7000):
	tarifa = 0.05
	taxa = 30
	valor = (peso * 0.05) + 30
	print(valor)
else: 
	tarifa = 0.06
	taxa = 35
	valor = (peso * 0.06) + 35
	print(valor)
	