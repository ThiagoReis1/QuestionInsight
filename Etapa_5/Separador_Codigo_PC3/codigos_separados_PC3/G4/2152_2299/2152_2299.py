from numpy import*

vet = array(eval(input("digite a matricula")))

m = 0

for i in range(size(vet)):
	if((vet[i]%2) != 0 ):
		m += 1

cont = zeros(m, dtype=int)

k = 0

for i in range(size(vet)):
	if((vet[i]%2) != 0 ):
		cont[k] = vet[i]
		k += 1
	
	

print(cont)