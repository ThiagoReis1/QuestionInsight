from numpy import *

vet= array(eval(input("digite vetor: ")))
perimetro = 0

for i in range(size(vet)):
	perimetro = perimetro + vet[i]
print(perimetro)


quantidade = 0

for i in range(size(vet)):
	if(vet[i] >= 5):
		quantidade = quantidade +1 
print(quantidade)
		
