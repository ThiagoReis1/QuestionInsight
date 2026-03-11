from numpy import* 

cont = zeros (4,dtype = int)
clinica = input('').upper().split(',')


for v in clinica:
	if v == 'O':
		cont[0] += 1
	elif v == 'D':
		cont[1] += 1
	elif v == 'N':
		cont[2] += 1
	elif v == 'C':
		cont[3] += 1
print(cont)