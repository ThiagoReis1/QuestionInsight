laranjas = float(input("valor comprado:"))

if laranjas < 6:
	total = laranjas * 0.75
	print(round(total,2))
else:
	total = laranjas * 0.60
	print(round(total,2))