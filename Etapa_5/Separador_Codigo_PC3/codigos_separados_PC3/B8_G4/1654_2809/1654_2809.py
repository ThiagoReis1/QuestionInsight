from numpy import*

est = input(":").split(',')

vet = zeros(5, dtype = int)

for i in range(size(est)):
	if est[i] == 'AM':
		vet[0] = vet[0] + 1
	elif est[i] == 'PE':
		vet[1] = vet[1] + 1
	elif est[i] == 'MG':
		vet[2] = vet[2] + 1
	elif est[i] == 'SP':
		vet[3] = vet[3] + 1
	elif est[i] == 'RS':
		vet[4] = vet[4] + 1
print(max(vet))
print(vet)