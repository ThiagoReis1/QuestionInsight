from numpy import*
vet = array(eval(input()))
for i in range(size(vet)):
	if vet[i] == 0:
		vet[i] = 9**2
	else:
		vet[i] = (vet[i] - 1)**2
print(vet)