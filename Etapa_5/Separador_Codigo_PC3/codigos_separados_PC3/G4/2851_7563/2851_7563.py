from numpy import*

vet = array(eval(input("Soma todos elementoos de um vetor: ")))

soma = 0 

for x in range(size(vet)):
	soma = soma + vet[x]
	if (vet[x] == 99):
		soma = soma - 99 
		soma = soma * 2 
	
print(soma)
