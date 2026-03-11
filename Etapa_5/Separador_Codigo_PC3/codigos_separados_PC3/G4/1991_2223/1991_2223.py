amino = input("Informe o aminoacido: ").upper()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if(amino == "GLICINA" or amino == "PROLINA" or amino == "SERINA"):
	if(amino == "GLICINA"):
		peso = C * 2 + H * 5 + N + O * 2
	elif(amino == "PROLINA"):
		peso = C * 5 + H * 10 + N + O * 2
	else:
		peso = C* 3 + H * 7 + N + O * 3
	print(round(peso,2))
else:
	print("Entrada:", amino)
	print("Dado Invalido")