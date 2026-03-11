n = int(input("Numero de laranjas:"))
if n<6:
	valor = 0.75*n
	print(round(valor, 2))
else:
	valor = 0.60*n
	print(round(valor, 2))