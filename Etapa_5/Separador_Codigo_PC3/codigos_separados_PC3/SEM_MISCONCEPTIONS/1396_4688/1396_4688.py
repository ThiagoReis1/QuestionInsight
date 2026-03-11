consumo = float(input("valor consumido: "))

if (consumo <= 300):
	print(round(consumo + consumo*10/100, 2))
else:
	print(round(consumo + consumo*6/100, 2))