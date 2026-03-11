from numpy import*
vetor = array(eval(input("Digite os pesos dos levantamentos: ")))
i = 0
j = 0
recorde = 307
while(i<size(vetor)):
	if(vetor[i] < recorde):
		j = j + 1
	i = i + 1
print(recorde)
print(j)