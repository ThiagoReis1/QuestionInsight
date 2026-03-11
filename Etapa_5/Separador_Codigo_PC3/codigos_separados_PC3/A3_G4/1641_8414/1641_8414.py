from numpy import*

vet = array(eval(input()), dtype=int)
cont = zeros(size(vet), dtype=int)

for  i in range(size(vet)): 
	if vet[i] % 3 == 0:
		cont += 1