con=float(input("Digite o consumo de minutos: "))

if (con<=100):
	x= (1.20 * con)
	print(round(x, 2))
else:
	y= (1.40 * con)+ 25.00
	print(round(y, 2))