n_laranjas = int(input("numero de laranjas:"))

if n_laranjas >= 6:
	print(round(n_laranjas * 0.60,2))
else:
	print(round(n_laranjas * 0.75,2))
	