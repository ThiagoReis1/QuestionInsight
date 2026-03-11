from numpy import *

cont=0
vet = eval(input("Nota: "))

for x in vet:
	if (x < 5):
		cont = cont + 1
cont1 = zeros(cont, dtype=int)
cont=-1

for x in range(size(vet)):
	if(vet[x] < 5):
		cont1[cont] = x
		cont = cont + 1
	
print(max(cont1))
print(cont1)
		