from numpy import *

vet = array(eval(input("Insira o vetor: ")))

i = 0
ganho = 0

while i < size(vet):
	if vet[i] == 1:
		ganho = ganho + 10
	elif vet[i] == 2:
		ganho = ganho + 5
	elif vet[i] == 3:
		ganho = ganho + 10
	elif vet[i] == 4:
		ganho = ganho + 5
	elif vet[i] == 5:
		ganho = ganho + 10
	elif vet[i] == 6:
		ganho = ganho + 5
	i += 1
print(ganho)