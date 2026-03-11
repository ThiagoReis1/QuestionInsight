from numpy import *

vet = array(eval(input()))
sum = 0
for i in range(size(vet)):
	sum += vet[i]
	if (vet[i] == 0):
		sum = 0
print(sum)