from numpy import *

vet = array(eval(input()))

turmas = 0

for i in range(size(vet)):
	if(vet[i] % 5 == 0):
		turmas = turmas +1
		
indices = zeros(turmas, dtype=int)

j = 0

for i in range(size(vet)):
	if(vet[i] % 5 == 0):
		indices[j] = i
		j = j + 1
		
print(turmas)
print(indices)