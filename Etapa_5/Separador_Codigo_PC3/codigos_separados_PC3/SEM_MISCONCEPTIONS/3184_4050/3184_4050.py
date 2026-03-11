from numpy import *
vetor = array(eval(input("Digite as letras: ")))

for i in range(size(vetor)):
	vetor[i] += str(range(-1, 0, 1))
print(vetor)