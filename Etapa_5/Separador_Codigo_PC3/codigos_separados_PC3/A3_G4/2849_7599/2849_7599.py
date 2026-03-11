from numpy import * 
vet = array(eval(input("numeros:")))
soma = 0
for i in vet:
	if(i==0):
		soma = 0
	else:
		soma = soma + i
print(soma)