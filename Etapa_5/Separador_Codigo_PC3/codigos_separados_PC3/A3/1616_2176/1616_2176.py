from numpy import *
vnome = array(eval(input("Digite o tipo de Magia: ")))
tam = size(vnome)
i = 0
vetor = array([[11,12,7,8,10]])

while(i<size(vnome)):
	if(vnome[i] == "GELO"):
		vetor[0] = 2
	elif(vnome[i] == "FOGO"):
		vetor[1] = 3
	elif(vnome[i] == "CHOQUE"):
		vetor[2] = 4
	elif(vnome[i] == "CONJURACAO"):
		vetor[4] = 8
	else:
  		vetor[i] = 10
	i = i + 1
print(vetor)