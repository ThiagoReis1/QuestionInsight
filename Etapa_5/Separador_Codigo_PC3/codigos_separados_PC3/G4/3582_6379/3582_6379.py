from numpy import *
vet = array(eval(input()))
cont = 0
for i in vet:
	if i > 160:
		i = i  - 25
	cont = cont + i
print(round(cont,2))