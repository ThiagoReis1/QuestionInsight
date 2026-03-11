numero = int(input("numero de laranjas compradas"))
if numero >= 6:
	compra = numero * 0.60 
	print(round(compra,  2))
else:
	compra = numero * 0.75
	print(round(compra,  2))