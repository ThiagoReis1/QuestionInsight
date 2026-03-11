A = int(input("Numero de laranjas compradas: "))

if A <= 6:
	x = A * 0.75
	print(round(x,2))
else:
	y = A * 0.60
	print(round(y,2))