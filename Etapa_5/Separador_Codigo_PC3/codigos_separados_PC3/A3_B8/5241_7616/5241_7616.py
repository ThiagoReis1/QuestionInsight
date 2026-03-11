consumo = float(input("Consumo: "))
taxa = 20
total = None

if consumo > 0 and consumo < 10:
	total = consumo * 2.0 + taxa
	print(total)
elif consumo >= 10 and consumo < 20:
	total = consumo * 2.5 + taxa
	print(total)
elif consumo >= 20 and consumo < 40:
	total = consumo * 2.75 + taxa
	print(total)
elif consumo >= 40:
	total = consumo * 3.0 + taxa
	print(total)