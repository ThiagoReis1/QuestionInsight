from numpy import *

vet = input("nacionalidades: ").upper().split(',')
cont = zeros(5, dtype=int)

for x in vet:
	if (x == 'AR'):
		cont[0] = cont[0] + 1
	elif (x == 'BR'):
		cont[1] = cont[1] + 1
	elif (x == 'CL'):
		cont[2] = cont[2] + 1
	elif (x == 'CO'):
		cont[3] = cont[3] + 1 
	elif (x == 'UY'):
		cont[4] = cont[4] + 1 

print(max(cont))
print(cont)