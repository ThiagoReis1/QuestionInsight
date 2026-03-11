consumo = int(input("Consumo em kWh: "))
a = 0.6
b = 0.75
x = float((a*consumo) + 5.0)
y = float((b*consumo) + 16.0)


if(consumo <= 150):
	print(round(x,2))
else:
	print(round(y,2))
