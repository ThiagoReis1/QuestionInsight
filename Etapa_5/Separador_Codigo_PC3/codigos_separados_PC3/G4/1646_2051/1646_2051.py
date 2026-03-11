from numpy import *


vet = array(eval(input("Valores: ")))
i=0

for x in range(size(vet)):
	if(vet[x] <= 50):
		i=i+1

cont = zeros(i, dtype=int) 

l = 0

for k in range(size(vet)):
	if(vet[k] <= 50):
		cont[l] = k
		l =+ 1
	
print(i)
print(cont)




