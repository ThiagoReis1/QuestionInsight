nome= input("Nome do aminoacido: ")
if(nome.upper() == "GLICINA"):
	peso = 2*12.011 + 5*1.0079 + 14.00674 + 2*15.9994
	print(round(peso,2))
elif(nome.upper() == "PROLINA"):
	peso = 5*12.011 + 10*1.0079 + 14.00674 + 2*15.9994
	print(round(peso,2))
elif(nome.upper() == "SERINA"):
	peso = 3*12.011 + 7*1.0079 + 14.00674 + 3*15.9994
	print(round(peso,2))
else:
	print("Entrada: ",nome)
	print("Dado Invalido")
