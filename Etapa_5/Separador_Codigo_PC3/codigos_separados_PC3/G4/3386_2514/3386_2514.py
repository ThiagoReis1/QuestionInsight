a = input(" unidade:")
b = float(input(" angulo: "))
if (a == "G"):
	a = 0.0174533 * b
	print(round(a,2))
else:
	a = b / 0.0174533
	print(round(a,2))