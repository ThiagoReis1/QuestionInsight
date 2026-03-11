from numpy import *

vet = array(eval(input("Digite o vetor")))
i = 0
cont = 0
while(i<size(vet)):
	if(vet[i]>=70):
		cont = cont + 1
	i = i + 1

vetAp = zeros(cont, dtype=int)

i = 0
j = 0
while(i<size(vet)):
	if(vet[i]>=70):
		vetAp[j] = i
		j = j + 1
	i = i + 1
		
print(cont)
print(vetAp)

