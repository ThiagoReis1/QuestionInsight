from numpy import *

vet = array(eval(input("")))
cont = 0
vn = []
for i in range(size(vet)):
	if vet[i]%3 == 0:
		cont = cont + 1
for i in range(size(vet)):
	if vet[i]%3 == 0:
		vn.append(i)
print(cont)
print(array(vn))
		
		