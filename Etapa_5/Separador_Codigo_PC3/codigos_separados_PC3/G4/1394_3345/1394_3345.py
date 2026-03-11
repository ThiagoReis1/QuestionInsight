h = float(input("Quantidade de horas: "))
v1 = h * 50
v2 = ((h - 20) * 70) + (50*20)

if (h <= 20):
	print(round(v1, 2))
else:
	print(round(v2, 2))