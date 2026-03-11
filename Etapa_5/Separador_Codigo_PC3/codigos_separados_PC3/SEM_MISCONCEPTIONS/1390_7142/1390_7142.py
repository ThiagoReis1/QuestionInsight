consumo = float(input("Informe o consumo de minutos de um cliente: "))

if(consumo <= 100):
	total = consumo*1.20
	print(round(total, 2))
else:
	total = consumo*1.40+25
	print(round(total, 2))