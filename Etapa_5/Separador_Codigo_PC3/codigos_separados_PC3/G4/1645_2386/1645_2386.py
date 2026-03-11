from numpy import*
from math import*

#vetor valores dos saques
Vet = array(eval(input()))

t = 0

for a in range(0, size(Vet)):
	if(Vet[a]>=2000):
		t = t + 1

NV = zeros(t, int)	

j = 0

for a in range(size(Vet)):
	if(Vet[a]>=2000):
		NV[j] = a
		j = j + 1
		

		
		
	

#saidas
print(t)
print(NV)



