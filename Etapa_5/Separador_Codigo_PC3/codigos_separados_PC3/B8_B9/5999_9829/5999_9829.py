compra = int(input("Digite o numero de laranjas compradas: "))

if (compra < 6):
	laranja = 0.75
	total = laranja*compra
	print(round(total,2))
elif (compra >= 6):
	laranja = 0.6
	total = laranja*compra
	print(round(total,2))
	
