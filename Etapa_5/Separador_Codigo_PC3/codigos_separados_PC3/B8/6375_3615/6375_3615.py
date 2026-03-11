from numpy import *

entrada = input()
entrada = entrada.split(',')
vet = zeros(4, int)

for i in range(size(entrada)):
	if entrada[i] == "A": vet[0] +=1
	elif entrada[i] == "B": vet[1] +=1
	elif entrada[i] == "C": vet[2] +=1
	elif entrada[i] == "D": vet[3] +=1
print(vet)