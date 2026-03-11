consumo=float(input("Digite o consumo:"))
tarifa=(consumo*1.20)
tarifa1=((consumo*1.40)+25.00)
if(consumo<=100):
	print(round(tarifa,2))
else:
	print(round(tarifa1,2))