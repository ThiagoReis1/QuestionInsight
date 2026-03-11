from math import*
from numpy import*
vetor = input("digite a etnia:").split(',')
cont = zeros(5, dtype = int)
i = 0
for i in range(len(vetor)):
	if (vetor[i] == "B"):
		cont[0] = cont[0] + 1
	elif (vetor[i] == "PA"):
		cont[1] = cont[1] + 1
	elif (vetor[i] == "PR"):
		cont[2] = cont[2] + 1
	elif (vetor[i] == "A"):
		cont[3] = cont[3] + 1
	elif (vetor[i] == "I"):
		cont[4] = cont[4] + 1

print(max(cont))
print(cont)
