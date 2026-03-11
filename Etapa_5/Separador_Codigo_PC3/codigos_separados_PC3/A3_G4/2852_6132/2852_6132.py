from numpy import *
vet = array(eval(input("insira um vetor: ")))

soma = 0
cont = 0
for i in range(size(vet)): 
	while vet[i]!= 88:
		soma = sum(vet[i])
		if vet[i] == 88:
			cont = cont + 1
			soma = (sum(vet[i])-(cont*88))

print(soma)