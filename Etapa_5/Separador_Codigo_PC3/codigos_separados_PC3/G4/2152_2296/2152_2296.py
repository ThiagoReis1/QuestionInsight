from numpy import*

vet = array(eval(input()))

m = 0

for i in range(size(vet)):
	if ((vet[i]%2) != 0):
		m += 1
		
cont = zeros(m, dtype=int)

p = 0

for i in range(size(vet)):
	if ((vet[i]%2) != 0):
		cont[p] = vet[i]
		p += 1
		
print(cont)