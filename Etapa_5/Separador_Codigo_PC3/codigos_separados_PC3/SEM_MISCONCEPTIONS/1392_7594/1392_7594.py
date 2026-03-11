consumo_agua = float(input("Consumo de agua em m3: "))

if consumo_agua>=10:
	print(round(consumo_agua*3.5+30, 2))
else:
	print(round(consumo_agua*3+30, 2))