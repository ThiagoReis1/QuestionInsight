from numpy import *

vet = array(eval(input()), dtype=int)
newvet = zeros(size(vet), dtype=int)

for i in range(size(vet)):
	newvet[i] = vet[i]*2
	
print(newvet)