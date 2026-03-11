from numpy import*

string = input().upper().split(',')
vet = zeros(4, dtype=int)

for i in range(size(string)):
	if string[i] == 'E':
		vet[0] += 1
	elif string[i] == 'V':
		vet[1] += 1
	elif string[i] == 'A':
		vet[2] += 1
	elif string[i] == 'D':
		vet[3] += 1
		
print(vet)