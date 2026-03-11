consumo = int(input("digite o consumo de agua: "))

if (consumo < 10):
	total = 20 + (2 * consumo)
	print(round(total, 2))
elif ((consumo >= 10) and (consumo < 20)):
	total = 20 + (2.5 * consumo)
	print(round(total, 2))
elif((consumo >= 20) and (consumo < 40)):
	total = 20 + (2.75 * consumo)
	print(round(total, 2))
elif (consumo >= 40):
	total = 20 + (3 * consumo)
	print(round(total, 2))