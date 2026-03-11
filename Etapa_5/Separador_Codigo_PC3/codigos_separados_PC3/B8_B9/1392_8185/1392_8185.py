from math import*
consumo = float(input("Qual foi o consumo do cliente? "))
if consumo < 10:
	tarifa = consumo*3 + 30
	print(round(tarifa, 2))
elif consumo >= 10:
	tarifa = consumo*3.5 + 30
	print(round(tarifa, 2))
