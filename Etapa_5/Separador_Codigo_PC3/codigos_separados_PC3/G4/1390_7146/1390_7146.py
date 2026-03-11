c = float(input("Digite o consumo de minutos:"))
cs_1 = c * 1.20
cs_2 = (c * 1.40) + 25.00

if (c <= 100):
	print(round(cs_1, 2))
else:
	print(round(cs_2, 2))