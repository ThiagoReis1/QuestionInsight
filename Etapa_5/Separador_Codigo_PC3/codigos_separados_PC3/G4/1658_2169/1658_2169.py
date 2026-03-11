from numpy import *
pais= input("").split(',')
vet= zeros(5, dtype = int)
for i in range(size(pais)):
	if( pais[i]== "CHN"):
		vet[0]= vet[0]+1
	elif(pais[i]== "JPN"):
		vet[1]= vet[1]+1
	elif(pais[i]== "KOR"):
		vet[2]= vet[2]+1
	elif(pais[i]== "MGL"):
		vet[3]= vet[3]+1
	else:
		vet[4]= vet[4]+1
print(max(vet))
print(vet)
	