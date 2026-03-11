from numpy import*
vetor = array(eval(input(" ")))
cont = 0 

for i in range(size(vetor)):
	if(vetor[i] >= 2000):
		cont[0] += 1

aux = zero(vetor, dtype = int)
x = 0

for i in range(size(vetor)):
	if(vetor[i] < 2000):
		aux[0] = 0

print(vetor)
print(aux)