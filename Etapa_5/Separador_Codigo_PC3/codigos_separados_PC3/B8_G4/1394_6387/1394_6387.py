a = float(input("Horas trabalhadas: "))

if (a <= 20):
	b = a * 50
	print(round(b,2))
elif (a >= 20):
	c = a - 20
	b = 20 * 50 + c * 70
	print(round(b,2))