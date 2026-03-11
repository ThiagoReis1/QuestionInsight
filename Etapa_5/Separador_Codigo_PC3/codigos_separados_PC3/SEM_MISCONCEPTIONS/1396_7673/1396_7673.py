a = float(input("valor consumido"))

if(a <= 300 ):
	total = a + 10/100 * a
	print(round(total, 2))
else:
	total = a + 6/100 * a
	print(round(total, 2))