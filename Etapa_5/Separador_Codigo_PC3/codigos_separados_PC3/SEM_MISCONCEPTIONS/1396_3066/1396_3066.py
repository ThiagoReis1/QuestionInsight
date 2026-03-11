consumo = float(input("digite: "))
limite = 300
if (consumo <= limite):
	gorjeta1 = consumo * 10 / 100
	consumo_total = consumo + gorjeta1
	print(round(consumo_total,2))
else:
	gorjeta2 = consumo * 6 / 100
	consumo_total2 = consumo + gorjeta2
	print(round(consumo_total2, 2))
	