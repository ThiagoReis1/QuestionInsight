from numpy import *
vetor = array(eval(input("Digite o vetor: ")))

soma = 0
i = 0

while i < size(vetor):
	soma = soma + vetor[i] * (1 + i)
	i = i + 1
	
print(soma)