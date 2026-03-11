from numpy import *

vet = array(eval(input("Vetor: ")))

saq = 0
for i in range(0, size(vet)):
	if(vet[i] >= 2000):
		saq = saq + 1

ind = zeros(saq, dtype= int)
k = 0
for j in range(0, size(vet)):
	if(vet[j] >= 2000):
		ind[k] = j
		k = k + 1
		
print(saq)
print(ind)