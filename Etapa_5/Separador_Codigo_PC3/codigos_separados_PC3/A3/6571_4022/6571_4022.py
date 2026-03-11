peso = float(input("peso: "))
taxa = 10

if (peso < 5):
	valor = taxa + 3.75
	total = valor
	print("total=", round(valor, 2))

elif peso == 5:
	valor = taxa + 4.75
	total = valor
	print("total=", round(valor, 2))

else:
	valor = taxa + 5.75
	total = valor
	print("total=", round(valor, 2))