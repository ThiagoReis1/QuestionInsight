from numpy import* 

vetor = array(eval(input("Informe o vetor: ")))

for i in range(size(vetor)):
	vetor[i] = vetor[i] * 2
print(vetor)