consumo = float(input("Consumo de energia: "))

if consumo <= 150:
	valor = consumo*0.60+5
	
else:
	valor = consumo*0.75+16
	
print(round(valor, 2))