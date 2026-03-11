consumo = int (input("Digite o consumo: "))

if (consumo <= 150):
	preco = 0.6*consumo + 5
	print (round(preco,2))

elif (consumo > 150):
	preco2 = 0.75*consumo + 16
	print (round(preco2,2))
	