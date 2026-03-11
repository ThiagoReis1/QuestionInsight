peso = int(input("digite o peso: "))

if peso < 5:
	taxa = 3.75
else:
	if peso == 5:
		taxa = 4.75
	else:
		taxa = 5.75
valor_total = 10 + taxa

print(round(valor_total, 2))

			