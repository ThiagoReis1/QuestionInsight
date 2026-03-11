from numpy import*
vet = array(eval(input()))
tap = 0
for i in range(size(vet)):
	if vet[i] >= 70:
		tap = tap + 1
aux = zeros(tap, dtype = int)
j = 0
for i in range(size(vet)):
	if vet[i] >= 70:
		aux[j] = i
		j = j + 1
print(tap)
print(aux) 
