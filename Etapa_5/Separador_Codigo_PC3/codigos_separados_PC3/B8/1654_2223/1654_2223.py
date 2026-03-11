from numpy import *
holmes = input("Informe os estados: ").split(',')

vet = zeros(5, dtype = int)

for i in holmes:
	if i == 'AM':
		vet[0] += 1
	elif i == 'PE':
		vet[1] += 1
	elif i == 'MG':
		vet[2] += 1
	elif i == 'SP':
		vet[3] += 1
	elif i == 'RS':
		vet[4] += 1
print(max(vet))
print(vet)