from numpy import *
notas = array(eval(input('Notas: ')))
aprov = 0
for i in range(size(notas)):
	if notas[i] >= 5:
		aprov += 1
print(aprov)
vet = zeros(aprov, dtype=int)
k = 0
for j in range(size(notas)):
	if notas[j] >= 5:
		vet[k] = j
		k = k + 1
		
print(vet)

	