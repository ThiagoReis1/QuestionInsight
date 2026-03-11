from numpy import * 

notas = input('').upper().split(',')
vet = zeros(4, dtype = int)

for i in notas:
	if i == 'C':
		vet[0] += 1
	elif i == 'D':
		vet[1] +=1
	elif i == 'V':
		vet[2] += 1
	elif i == 'U':
		vet[3] += 1
		
print(vet)
		
	