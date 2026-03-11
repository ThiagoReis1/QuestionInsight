from numpy import *

cont = zeros(5, dtype=int)

vet = input("estado: ").upper().split(',')

for x in vet:
	if (x == 'AC'):
		cont[0] = cont[0] + 1
	elif (x == 'AM'):
		cont[1] = cont[1] + 1
	elif (x == 'PA'):
		cont[2] = cont[2] + 1
	elif (x == 'RO'):
		cont[3] = cont[3] + 1
	elif (x == 'RR'):
		cont[4] = cont[4] + 1

print(max(cont[0],cont[1],cont[2],cont[3],cont[4]))
print(cont)