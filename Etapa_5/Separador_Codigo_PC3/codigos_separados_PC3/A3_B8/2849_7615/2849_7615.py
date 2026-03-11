from numpy import *
vetor= array(eval(input("Digite o valor: ")))

soma= 0
for i in range(size(vetor)):
	if vetor[i] != 0:
		soma= soma + vetor[i]
	elif vetor[i] == 0:
		soma= 0

print(soma)