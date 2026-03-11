from numpy import*

vet1 = array(eval(input()))
cont = 0

for v in vet1:
	if v >= 70:
		cont += 1
print(cont)

vet2 = zeros(cont, dtype=int)
j = 0

for i in range(size(vet1)):
	if vet1[i] >= 70:
		vet2[j] = i
		j += 1
print(vet2)