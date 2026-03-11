from numpy import*
vet = 4 * [0]
paciente = str(input())

for i in range(len(paciente)):
	if paciente[i] == 'O':
		vet[0] += 1
	elif paciente[i] == 'D':
		vet[1] += 1
	elif paciente[i] == 'N':
		vet[2] += 1
	elif paciente[i] == 'C':
		vet[3] += 1

vet = array(vet)
print(vet)
