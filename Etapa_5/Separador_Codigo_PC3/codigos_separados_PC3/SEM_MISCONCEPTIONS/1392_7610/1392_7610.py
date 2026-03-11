consumo = float(input("digite o consumo: "))

if consumo< 0:
	print(round(consumo + 30.0 * 3.5, 2))
else: 
	print(round(consumo + 30.0 * 3.0, 2))
