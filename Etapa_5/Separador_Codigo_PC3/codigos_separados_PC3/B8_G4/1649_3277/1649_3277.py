from numpy import *
from numpy.linalg import *

cont = zeros(5, dtype=int)

vet = input("Cor dos olhos: ").upper().split(',')

	
for x in vet:
	if (x == 'P'):
		cont[0] = cont[0] + 1
	elif (x == 'C'):
		cont[1] = cont[1] + 1
	elif (x == 'M'):
		cont[2] = cont[2] + 1
	elif (x == 'V'):
		cont[3] = cont[3] + 1
	elif (x == 'A'):
		cont[4] = cont[4] + 1
print(max(cont[0],cont[1],cont[2],cont[3],cont[4]))
print(cont)
