consumo= float(input("minutos consumidos: "))
if (consumo <= 100):
	print (round(consumo*1.20 , 2))
else:
	print (round(25.00 + consumo*1.40))