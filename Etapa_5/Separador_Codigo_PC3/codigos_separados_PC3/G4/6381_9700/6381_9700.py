from numpy import *
cont=input().upper().split(",")
vet=zeros(4, dtype=int)

for i in range (len(cont)):
	if cont[i] =="C":
		vet[0]= vet[0]+1
	elif cont[i] =="O":
		vet[1]=vet[1]+1
	elif cont[i] =="P":
		vet[2]=vet[2]+1
	else:
		vet[3]=vet[3]+1
print(vet)




