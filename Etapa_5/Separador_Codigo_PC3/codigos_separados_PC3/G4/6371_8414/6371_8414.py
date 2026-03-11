from numpy import*

vet = array(eval(input(" insira o codigo: ")))
cont = zeros(size(vet), dtype=int)
i = 0

for i in range(size(vet)): 
	if vet[i] > 0 and vet[i] < 10: 
		cont[i] = (vet[i] - 1)**2

	else:
		cont[i] = 9**2
		
		
print(cont)
	