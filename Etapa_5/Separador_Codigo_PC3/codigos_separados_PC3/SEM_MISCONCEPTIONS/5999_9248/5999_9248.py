x = int(input('quantidade de laranjas compradas: '))

if(x < 6):
	valor = (0.75 * x)
	print(round(valor, 2))
	
else:
	valor = (0.6 * x)
	print(round(valor, 2))