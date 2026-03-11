from numpy import *

vet = array(eval(input("Digite os numeros sorteados: ")))
cont = zeros(37, dtype=int)

for i in range(size(cont)):
	for j in vet:
		if(i == j):
			cont[i] += 1
			
print(cont)