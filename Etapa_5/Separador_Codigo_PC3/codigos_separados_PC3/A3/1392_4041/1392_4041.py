consumo_de_agua = float(input("seu consumo de agua: "))

tarifa = 30.0
consumo = 10.0
if (consumo_de_agua>=consumo):
	print(round(consumo_de_agua*3.5+30.0, 2))
else:
	print(round(consumo_de_agua*3.0+30.0, 2))
