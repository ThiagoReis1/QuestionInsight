consumo = float(input("Digite o consumo de agua em m^3: "))
taxa = 30.0
if (consumo < 10):
	total1 = consumo*3
	total2 = total1+taxa
	print(round(total2,2))
else:
	total3 = consumo*3.5
	total4 = total3+taxa
	print(round(total4,2))

