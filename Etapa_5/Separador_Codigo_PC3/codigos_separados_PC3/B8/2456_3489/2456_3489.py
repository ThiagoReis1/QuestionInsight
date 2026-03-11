mes = float(input("insira o valor da mensalidade: "))
kid = float(input("insira o numero de criancas: "))


if (kid == 1) or (kid == 2) or (kid >= 3) :
	if (kid == 1) :
		valor = mes * kid - (mes * 10/100)
	elif (kid == 2) :
		valor = (mes - (mes * 30/100)) * kid
	elif (kid >= 3) :
		valor = (mes - (mes * 40/100)) * kid
	print(round(valor, 2))