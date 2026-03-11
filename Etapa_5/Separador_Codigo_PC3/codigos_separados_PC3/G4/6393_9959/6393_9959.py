from numpy import * 

vet = array(eval(input()))
vet2 = zeros(size(vet), dtype=int)

for i in range (size(vet)):
	if vet[i] == 9:
		vet2[i] = 0 ** 3
	else:
		vet2[i] = (vet[i] + 1) ** 3

print(vet2)