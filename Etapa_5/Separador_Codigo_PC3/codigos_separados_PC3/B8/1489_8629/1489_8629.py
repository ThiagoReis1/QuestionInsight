consumo = float(input("consumo: "))

if consumo > 0  and consumo < 150:
	total = consumo*0.60 + 5
	print(round(total,2))
elif consumo >= 150 and consumo < 250:
	total = consumo*0.65 + 8
	print(round(total,2))
elif consumo >= 250 and consumo < 350:
	total = consumo*0.70 + 12
	print(round(total,2))
elif consumo >= 350 or consumo > 350:
	total = consumo*0.75 + 16
	print(round(total,2))