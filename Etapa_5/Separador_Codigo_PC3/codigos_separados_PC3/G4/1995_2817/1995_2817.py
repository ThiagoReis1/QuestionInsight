nome = input("");

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(nome.lower() == "aspartato" or nome.lower() == "cisteina" or nome.lower() == "metionina"):
	if(nome.lower() == "aspartato"):
		peso = 4*C+6*H+N+4*O
	elif(nome.lower() == "cisteina"):
		peso = 3*C+7*H+N+2*O+S
	else:
		peso = 5*C+11*H+N+2*O+S
	
	print(round(peso,2))
else:
	print("Entrada:", nome.lower())
	print("Dado Invalido")