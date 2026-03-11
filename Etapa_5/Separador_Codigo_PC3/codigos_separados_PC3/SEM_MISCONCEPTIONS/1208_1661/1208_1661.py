from numpy import *
vetor = array(eval(input("Digite os pesos dos levantamentos: ")))
i = 0
k = 0
recorde = 98.48
while(i<size(vetor)):
	if(vetor[i] < recorde):
		k = k + 1
	i = i + 1
print(recorde)
print(k)