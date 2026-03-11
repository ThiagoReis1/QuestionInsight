from numpy import * 
vet=input().upper().split(",")
cont = zeros(5, dtype=int)
C=0
P=0
V=0
A=0
for i in arange(size(vet)):
	if( vet[i] == 'P'):
		cont[0]= cont[0] + 1
	elif( vet[i] == 'C'):
		cont[1]= cont[1] + 1
	elif( vet[i] == 'M'):
		cont[2]= cont[2] + 1
	elif( vet[i] == 'V'):
		cont[3]= cont[3] + 1
	elif( vet[i] == 'A'):
		cont[4]= cont[4] + 1
print(max(cont))
print(cont)
	