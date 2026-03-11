x = int(input("numero de laranjas: "))
p = 0.75
y = 0.60

if x>=6:
	a = x * y
	print(round(a, 2))
else:
	b = x * p
	print(round(b, 2))
		