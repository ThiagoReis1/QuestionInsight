from numpy import *
vetor = array(eval(input("Digite o vetor: ")))
i = 0
q = 0
while(i < size(vetor)):
	if(vetor[i] > 8.95):
		q = q + 1
	i = i + 1
print("8.95")
print(q)