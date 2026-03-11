a = float(input("quantidade de combustivel comum: "))


if a < 17.5:
	print(round(a + 10.5, 2))
elif a >= 17.5 and a < 35.0:
	print(round(a + 14.0, 2))
elif a >= 35.0 and a < 50.0:
	print(round( a + 18.6, 2))
elif a >= 50.0:
	print(round(a + 24.5, 2))
	