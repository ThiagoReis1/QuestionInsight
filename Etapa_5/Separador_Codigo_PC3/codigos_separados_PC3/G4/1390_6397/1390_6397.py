a = float(input("Consumo de minutos de um cliente:"))

if (a <= 100):
	b = a * 1.20
	print(round(b,2))
else:
	e = (a*1.40) + 25 
	print(round(e,2))