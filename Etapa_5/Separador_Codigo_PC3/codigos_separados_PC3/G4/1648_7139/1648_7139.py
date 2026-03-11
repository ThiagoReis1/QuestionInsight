from numpy import *

vet1 = array(eval(input("Frequencia:")))

reprov = 0 

for i in range (size(vet1)):
	if (vet1[i] < 70):
		reprov = reprov + 1
		
print(reprov)

vet2 = zeros(reprov, dtype=int)
j = 0 

for i in range(size(vet1)):
	if (vet1[i] < 70):
		vet2[j] = i
		j = j + 1
		
print(vet2)