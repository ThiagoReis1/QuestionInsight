from numpy import *
vetor = array(eval(input("pontos: ")))

cont = 0
pontos = 100
while (cont < len(vetor)):
	if (vetor[cont] == 1):
		pontos = pontos * 5 
	elif (vetor[cont] == 2):
		 pontos = pontos * 3
	elif (vetor[cont] == 3):
		 pontos = pontos 
	elif (vetor[cont] == 4):
		 pontos = pontos / 2
	cont += 1
		
print(round(pontos, 2))