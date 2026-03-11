from numpy import *


vet=array(eval(input("Codigo: ")))

#ma=zeros([shape(mat)[0], shape(mat)[1]], dtype=int)

for i in range(size(vet)):
	vet[i] = vet[i]**2
		
print(vet)