from numpy import *

vet = input("Digite a frase: ")
vet1 = vet.islower() and vet.isupper()

for i in range(len(vet)):
	if(vet[i].islower() != vet[i].isupper()):
		saida = saida + vet1[i]
print(saida)