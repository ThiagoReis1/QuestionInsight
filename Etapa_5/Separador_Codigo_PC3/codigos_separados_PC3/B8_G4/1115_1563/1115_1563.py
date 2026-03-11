X = float(input("Salario atual: "))
Y = int(input("Codigo do cargo: "))
if ((X >= 0) and ((Y == 101) or (Y == 102) or (Y == 103) or (Y == 104))):
	if (Y == 101):
		Z = (X + X*(0.0080))
		Z = round(Z,2)
	else:
		if (Y == 102):
			Z = (X+X*(0.0065))
			Z = round(Z,2)
		else:
			if (Y == 103):
				Z = (X+X*( 0.0060))
				Z = round(Z,2)
			else: 
				if (Y == 104):
					Z = (X+X*(0.0055))
					Z = round(Z,2)
	print ("Entradas: R$ ", X, " e codigo ", Y)
	print ("Novo salario: R$ ", Z)
else:
	print ("Entradas: R$ ", X, " e codigo ", Y)
	print ("Dado invalido")