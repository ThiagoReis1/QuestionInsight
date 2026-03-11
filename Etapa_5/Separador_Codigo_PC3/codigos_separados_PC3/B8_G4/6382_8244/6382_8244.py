from numpy import*

vet = array(eval(input()))
vet1 = zeros(size(vet), dtype=int)
j = 0

for i in range(size(vet)):
	if vet[i] >= 0 and vet[i] < 9:
		vet1[j] = (vet[i]+1)**2
	elif i == 9:
		vet1[j] = 1
	j += 1
print(vet1)