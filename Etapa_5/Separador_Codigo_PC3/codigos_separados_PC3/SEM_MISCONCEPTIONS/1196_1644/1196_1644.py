from numpy import *
vetor = array(eval(input("Digite o vetor: ")))
i = 0
k = 0
cont = 0
while(i < size(vetor)):
	if(vetor[i] > -60 and vetor[i] < 60):
		i = i + 1
	else:
		cont = cont + 1
		i = i + 1
tamanho = size(vetor) - cont
vetor1 = array(zeros(tamanho, dtype = float))
i = 0
while(i < size(vetor)):
	if(vetor[i] < 60 and vetor[i] > -60):
		vetor1[k] = vetor[i]
		i = i + 1
		k = k + 1
	else:
		i = i + 1
print(vetor1)