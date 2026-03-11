from numpy import*
olhos=input("olhos:").upper().split(",")

vet=zeros(5,dtype=int)

for i in range(size(olhos)):
	if olhos[i]=="P":
		vet[0]=vet[0]+1
	elif olhos[i]=="C":
		vet[1]=vet[1]+1
	elif olhos[i]=="M":																							
		vet[2]=vet[2]+1
	elif olhos[i]=="V":
		vet[3]=vet[3]+1
 	elif olhos[i]=="A":
		vet[4]=vet[4]+1
	print(i)
print(vet)		