qtd = int(input("digite numero de bilhetes: "))
tipo = input("tipo de acomodacao: ")

Rede = 500.00
Camarote = 1200.00
Suite = 1500.00

if((tipo=="rede") or (tipo=="camarote") or (tipo=="suite")):
	if(tipo=="rede"):
		valor = qtd * Rede
	elif(tipo=="camarote"):
		valor = qtd * Camarote
	elif(tipo=="suite"):
		valor = qtd * Suite
	print(round(valor, 2))
else:
	print("acomodacao invalida")


