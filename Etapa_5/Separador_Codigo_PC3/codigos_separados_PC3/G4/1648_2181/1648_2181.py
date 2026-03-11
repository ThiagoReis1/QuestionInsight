from numpy import *
vet = array(eval(input("Digite um vetor de frequencia: ")))

soma = 0
for i in range(size(vet)):
	if	(vet[i] < 70):
		soma = soma + 1
print(soma)  


v = zeros(soma, dtype = int)
cont = 0
for j in range(size(vet)):
	if(vet[j] < 70):
		v[cont] = j
		cont = cont + 1
print(v)		