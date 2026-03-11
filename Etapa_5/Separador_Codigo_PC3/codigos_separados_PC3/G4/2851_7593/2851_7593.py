from numpy import * 

vet = array(eval(input("valores: ")))
soma = 0
for i in range(size(vet)):
	if(vet[i] == 99):
		soma = soma * 2
	else:
		soma = soma + vet[i]
print(soma)