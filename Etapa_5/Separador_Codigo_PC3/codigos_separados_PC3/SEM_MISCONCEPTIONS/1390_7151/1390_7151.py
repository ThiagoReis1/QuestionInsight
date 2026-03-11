consumo=float(input("digite consumo"))

if consumo<=100:
	print (round( consumo *1.20,2))
	
if consumo>100:
	valor_da_conta= 25 + 1.4*consumo
	print (round(valor_da_conta,2))