tarifa1 = 1.20
tarifa2 = 1.40
taxa = 25
consumo = int(input("valor do consumo: "))
consumo1 = (consumo * tarifa1)
consumo2 = (consumo * tarifa2) + taxa
if(consumo < 100):
	print(round(consumo1,2))
else:
	print(round(consumo2,2))
	

