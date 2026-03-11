a = float (input("Área a ser Fertilizada: "))

if (a <= 10000):
	x = 5 * a
	print(round(x,2))
else:
	x = ((a // 10000)*5*10000) + 4*(a - 10000)
	print(round(x,2))