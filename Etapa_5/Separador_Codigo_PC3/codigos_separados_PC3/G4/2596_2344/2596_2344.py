from numpy import *

vet= array(eval(input("Digite um vetor de oscilacoes de demanda:")))

cont= 0

for i in range(1,size(vet)):
	if(vet[i] >= vet[0]):
		cont= cont + 1
		print(i)
		
print(cont)
