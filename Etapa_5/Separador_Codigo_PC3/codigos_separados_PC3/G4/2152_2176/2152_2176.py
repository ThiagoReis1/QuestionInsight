from numpy import *
vet = array(eval(input("Digite o vetor")))
i = 0
cont = 0
for i in range(size(vet)):
	if(vet[i]%2!=0):
		cont = cont + 1

j = 0
valor = str(vet[i])
vetN = zeros(cont, dtype=int)
for i in range(size(vet)):
	if(vet[i]%2!=0 and len(valor)==8):
		vetN[j] = vet[i]
		j = j + 1
print(vetN)
