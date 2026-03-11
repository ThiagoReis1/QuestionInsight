consumo = float(input("digite o consumo"))

if consumo <= 100:
	t = consumo * 1.20
	print(round(t, 2))
else:
	t = (consumo * 1.40)+ 25
	print(round(t, 2))