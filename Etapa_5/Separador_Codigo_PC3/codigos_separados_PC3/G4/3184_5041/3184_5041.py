from numpy import *

vet = array(eval(input("Digite as letras do alfabeto em ordem decrescente: ")))
vet1 = zeros(size(vet), dtype=str)

i = 0

for x in range(0, size(vet)):
	vet1[i] = vet[x]
	i = i + 1
	
print(vet1)
	