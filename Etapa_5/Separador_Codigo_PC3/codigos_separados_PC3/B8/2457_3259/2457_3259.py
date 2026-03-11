bilhetes = int(input("Quantidade de bilhetes: "))
acomodacao = input("rede,camarote ou suite: ")

if ( acomodacao =="rede" ) or (acomodacao =="camarote") or (acomodacao =="suite"):
	
	if (acomodacao == "rede"):
		valor = float(bilhetes * 500)
		print(round(valor, 2))
	elif (acomodacao == "camarote"):
		valor = float(bilhetes * 1200)
		print(round(valor, 2))
	elif (acomodacao == "suite"):
		valor = float(bilhetes * 1500)
		print(round(valor, 2))
else:
	print("acomodacao invalida")
	
