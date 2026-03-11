from numpy import *
vet = array(eval(input()))
for i in range(0, size(vet)):
	if vet[i] == 0:
		vet[i] = 9**3
	else:
		vet[i] = (vet[i] - 1)**3
	i += 1
print(vet)