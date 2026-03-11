from numpy import*
vetor = array(eval(input("Dano de ataque: ")))
i = 0 
peso = 1
cont = 0
while(i<size(vetor)):
	cont = cont + vetor[i] * peso
	peso = peso + 1
	i = i + 1
print(cont)

