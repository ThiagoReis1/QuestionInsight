x = float(input("Leia o valor de x :"))

if (x <= 1):
	a = 1
	print(round(a, 2))
elif (1 < x <= 2):
	b = 2
	print(round(b,2))
elif (2 < x <= 3):
	c = x ** 2
	print(round(c, 2))
else:
	d = x ** 3
	print(round(d, 2))