from math import*
nome = input("Digite o nome do aminoacido: ")

if ((nome.upper() != "GLICINA") and (nome.upper() != "PROLINA") and (nome.upper() != "SERINA")):
	print("Entrada:",nome)
	print("Dado Invalido")
elif(nome.upper() == "GLICINA"):
	var = (12.011)*2+(1.0079)*5+(14.00674)+(15.9994)*2
	print(round(var, 2))
elif(nome.upper() == "PROLINA"):
	var = (12.011)*5+(1.0079)*10+(14.00674)+(15.9994)*2
	print(round(var, 2))
elif(nome.upper() == "SERINA"):
	var = (12.011)*3+(1.0079)*7+(14.00674)+(15.9994)*3
	print(round(var, 2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")