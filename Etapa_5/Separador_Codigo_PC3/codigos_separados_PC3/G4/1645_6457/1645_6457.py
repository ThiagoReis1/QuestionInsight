from numpy import *

vet = array(eval(input("Digite o vetor: ")))

cont = 0
x = 0

for i in range(size(vet)):
	if vet[i] >= 2000:
		cont = cont + 1
print(cont)

v = zeros(cont,dtype=int)

for i in range(size(vet)):
	if vet[i] >= 2000:
		v[x] = i
		x = x + 1
print(v)


	