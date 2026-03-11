from numpy import *

vet = array(eval(input("senha: ")))

j = 0
for i in vet:
	if i > 0 and i<10:
		j = j + 1
vet_final=zeros(j,dtype= int)

a = 0
for i in vet:
	vet_final[a] = i**2
	a = a + 1
print(vet_final)

