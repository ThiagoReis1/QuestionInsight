x = float(input())

if x <= 150:
	tarifa = (x * 0.6) + 5	
	print(round(tarifa, 2))
else:
	tarifa = (0.75 * x) + 16
	print(round(tarifa, 2))