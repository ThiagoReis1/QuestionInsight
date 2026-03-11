a = float(input("Consumo de agua: "))

if (a < 10):
	b = 2 * a + 20
	print(round(b,2))
elif (a >= 10 and a < 20):
	b = 2.5 * a + 20
	print(round(b,2))
elif (a >= 20 and a < 40):
	b = 2.75 * a + 20
	print(round(b,2))
elif (a >= 40):
	b = (3 * a) + 20
	print(round(b,2))