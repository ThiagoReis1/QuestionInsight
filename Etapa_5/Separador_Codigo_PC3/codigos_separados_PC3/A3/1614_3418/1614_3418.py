from numpy import*
vetor1 = array(input("Nomes: ").upper())
vetor2 = array(eval(input("Quantidade: ")))
i = 1
cont = 0
while i<size(vetor1) and i<size(vetor2):
	if(vetor1 == "BANANA"):
		cont = (cont + vetor[i]) * 0.97
		i = i + 1
	elif(vetor1 == "BIFE"):
		cont = (cont + vetor[i]) * 2.95
		i = i + 1
	elif(vetor1 == "FEIJOADA"):
		vcont = (cont + vetor[i]) * 1.27
		i = i + 1
	elif(vetor1 == "OMELETE"):
		cont = (cont + vetor[i]) * 1.4 
		i = i + 1
	elif(vetor1 == "TOMATE"):
		cont = (cont + vetor[i]) * 0.2
		i = i + 1
	else:
		cont = cont + vetor[i]
		i = i + 1
print(round(cont, 2))