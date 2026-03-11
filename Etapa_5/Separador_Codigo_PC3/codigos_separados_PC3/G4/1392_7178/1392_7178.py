a = float(input("digite o valor do consumo de agua: "))


if a <= 10:
	b = (a * 3.0) + 30
	print(round(b, 2))
else:
	c = (a * 3.50) + 30
	print(round(c, 2))