from numpy import * 

notas = array(eval(input("Notas: ")))

i = 0 

for j in range(size(notas)):
	if(notas[j] < 70):
		i = i + 1
		j = j + 1
print(i)

vet = zeros(i, dtype = int)
l = 0

for k in range(size(notas)):
	if(notas[k] < 70):
		vet[l] = k
		k = k + 1
		l = l + 1
print(vet)