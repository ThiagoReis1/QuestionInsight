from numpy import * 
vet = input("").split(',')

zet = zeros(5,dtype=int)

for i in range(size(vet)):
	if(vet[i] == 'P' ):
		zet[0] = zet[0] + 1
	if(vet[i] == 'C' ):
		zet[1] = zet[1] + 1
	if(vet[i] == 'R' ):
		zet[2] = zet[2] + 1
	if(vet[i] == 'L' ):
		zet[3] = zet[3] + 1
	if(vet[i] == 'B' ):
		zet[4] = zet[4] + 1
m = max(zet)
print(m)
print(zet)	