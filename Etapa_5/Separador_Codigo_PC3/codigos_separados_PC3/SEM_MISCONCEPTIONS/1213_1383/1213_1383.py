from numpy import *
vetor = array(eval(input("Informe o vetor: ")))
i = 0
q = 0
while(i < size(vetor)):
	if(vetor[i] > 217):
		q = q + 1
	i = i + 1
print("217")
print(q)