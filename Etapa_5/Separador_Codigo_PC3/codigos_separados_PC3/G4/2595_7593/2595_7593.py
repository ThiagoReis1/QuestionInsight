from numpy import *

vet =array(eval(input("receber: ")))

soma = 0

for i in range(1, size(vet)):
	if(vet[i] < 0) and (vet[i]<= vet[0]):
		print(i)
		soma = soma + 1
print(soma)
