#v[0] = numero minimo de acidentes 
#
from numpy import*

vet = array(eval(input("Digite o vetor: ")))

cont = 0

for i in range(1,size(vet)):
	if(vet[i] >= vet[0]):
		cont = cont + 1
		print(i)
print(cont)

























