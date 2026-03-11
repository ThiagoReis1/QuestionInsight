taxa = 30
tarifa_inf = 3
tarifa_sup = 3.5

consumo = float(input("insira consumo: "))
if (consumo <= 10):
	print(round(consumo*tarifa_inf+taxa, 2))
	
else:
	print(round(consumo*tarifa_sup+taxa, 2))