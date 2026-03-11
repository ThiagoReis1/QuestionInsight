from numpy import *

vet = array(eval(input("  ")))

q = 0
for i in range (size(vet)):
	if (vet[i] < 70):
		q = q + 1
		
print(q)	
vetor = zeros(q,dtype=int)


for i in range(size(vet)):	
	if (vet[i] > 70):
		vetor[i] = vet[i]
		
print(vetor)