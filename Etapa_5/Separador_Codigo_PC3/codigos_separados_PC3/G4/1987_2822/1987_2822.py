nome = input("Nome do aminoácido: ").upper()

if(nome == "ALANINA" or nome == "VALINA" or nome == "TIROSINA"):
	if(nome == "ALANINA"):
		peso = (3*12.011)+(7*1.00794)+(14.00674)+(2*15.9994)
	elif(nome == "VALINA"):
		peso = (5*12.011)+(11*1.00794)+(14.00674)+(2*15.9994)
	else:
		peso = (9*12.011)+(11*1.00794)+(14.00674)+(3*15.9994)
	print(round(peso,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")