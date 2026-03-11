from numpy import*

v=input("").split(',')

vet=zeros(5,dtype=int)

for i in range(size(v)):
	if(v[i]=="CHN"):
		vet[0]=vet[0]+1
	if(v[i]=="JPN"):
		vet[1]=vet[1]+1
	if(v[i]=="KOR"):
		vet[2]=vet[2]+1
	if(v[i]=="MGL"):
		vet[3]=vet[3]+1
	if(v[i]=="THA"):
		vet[4]=vet[4]+1
		
print(max(vet))
print(vet)