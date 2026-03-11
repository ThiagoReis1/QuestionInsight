from numpy import*

n = input().upper()

vet = zeros(4,dtype = int)

for i in n:
	if i == 'A':
		vet[0] = vet[0] + 1
	elif i == 'B':
		vet[1] = vet[1] + 1
	elif i== 'C':
		vet[2]= vet[2]+ 1
	elif i == 'D':
		vet[3] = vet[3] + 1
	
print(vet)

