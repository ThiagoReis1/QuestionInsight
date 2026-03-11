Med = input("Unidade em que a medida esta (A/H): ").upper()
valor = float(input("Valor da medida: "))

if (Med == 'H'):
	x = valor * 2.47105
	print(round(x, 2))
else:
	x = valor/2.47105
	print(round(x, 2))