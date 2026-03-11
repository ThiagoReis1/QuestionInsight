from numpy import*
vetor1 = array(eval(input("dig: ")))
vetor2 = array(eval(input("dig: ")))
cont = 0
soma = 0
while(cont<size(vetor1)):
	if(vetor2[cont] == "QUENTE"):
		soma = 90 * 0.005
	elif(vetor2[cont] == "MORNO"):
		soma = 45 * 0.005
	elif(vetor2[cont] == "FRIO"):
		soma = 0 * 0.005
	cont = cont + 1
print(round(soma, 2))