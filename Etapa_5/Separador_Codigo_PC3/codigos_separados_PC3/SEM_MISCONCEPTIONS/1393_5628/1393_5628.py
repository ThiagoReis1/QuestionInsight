taxa = 60

kg = float(input('Peso:  '))

if (kg < 5000):
	frete = (kg * 0.05)
	print(round(frete,2))
else:
	frete = (kg * 0.04) + taxa
	print(round(frete,2))