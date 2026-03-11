from numpy import *
vet = array(eval(input("")))
cont = 0
j = 0
for i in range(0, size(vet)):
	if(vet[i] % 2 != 0):
		cont += 1
z = zeros(cont, dtype = int)
for i in range(0, size(vet)):
	if(vet[i] % 2 != 0):
		z[j] = i
		j += 1
print(cont)
print(z)