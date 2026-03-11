consumo=int(input("Valor de consumo: "))
if(consumo<10):
	print(round(30+(3*consumo),2))
else:
	print(round(30+(3.5*consumo),2))