nome = input(" ")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if(nome == "GLICINA" or nome == "PROLINA"or nome == "SERINA"):
	if(nome == "GLICINA"):
		peso = 2*C + 5*H + N + 2*O
		print(round(peso,2))
	elif(nome == "PROLINA"):
		peso = 5*C + 10*H+N+2*O
		print(round(peso,2))
	elif(nome == "SERINA"):
		peso = 3*C+7*H+N+3*O
		print(round(peso,2))
	else:
		print("Entrada:",nome.upper())
		print("Dado Invalido")
else:
	print("Entrada:",nome.upper())
	print("Dado Invalido")
		


