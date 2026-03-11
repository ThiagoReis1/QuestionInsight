consumo = int(input("Digite o consumo de agua: "))
valor = 30.0
tarifa1 = 3.0
tarifa2 = 3.50
maior10 = valor+consumo*tarifa2
menor10 = valor+consumo*tarifa1
if consumo >= 10:
	print(round(maior10,2))
else:
	print(round(menor10,2))