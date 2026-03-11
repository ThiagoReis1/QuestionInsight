from numpy import *
vet = array(eval(input("Frequencia: ")))
reprov = 0

for i in range(size(vet)):
	if(vet[i] < 70):
		reprov += 1

indice = 0
j = 0
indice_vet = zeros(reprov,dtype=int)
for i in range(size(vet)):
	if(vet[i] <70):
		indice_vet[j] = indice
		j += 1
	indice += 1
	
print(reprov)
print(indice_vet)