consumo=float(input(" Qual o consumo de litros da agua : "))
taxa=30.00
tarifa1=taxa+consumo*3.00
tarifa2=taxa+consumo*3.50

if (consumo<10.0):
	print(round(tarifa1,2))
else:
	print(round(tarifa2,2))
