consumo = float(input("COnsumo: "))
if(consumo >= 10):
	tarifa = 3.50
	conta= tarifa*consumo + 30
	print(round(conta,2))
if(consumo< 10):
	tarifa = 3.00
	conta = tarifa*consumo + 30
	print(round(conta,2))