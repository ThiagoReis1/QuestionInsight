opcao = str(input())
angulo = float(input())

if opcao == 'R':
	gr = angulo/0.0174533
	print(round(gr, 2))
else:
	if opcao == 'G':
		rad = 0.0174533 * angulo
		print(round(rad,2))