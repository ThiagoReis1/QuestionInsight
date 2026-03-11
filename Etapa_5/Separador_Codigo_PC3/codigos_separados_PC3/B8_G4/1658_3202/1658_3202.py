from numpy import *
vet = input(" ").upper().split(',')
cont = zeros(5, dtype=int)

for x in vet:
	if (x == 'CHN'):
		cont[0] = cont[0] + 1
	elif (x == 'JPN'):
		cont[1] = cont[1] + 1
	elif (x == 'KOR'):
		cont[2] = cont[2] + 1
	elif (x == 'MGL'):
		cont[3] = cont[3] + 1
	elif (x == 'THA'):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)