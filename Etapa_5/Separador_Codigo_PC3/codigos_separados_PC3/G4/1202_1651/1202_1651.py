from numpy import *
vet=array(eval(input("qual eh o vetor?")))
maxi=40
i=0
j=0
while(i<size(vet)):
	if(vet[i]<=maxi):
		j=j+1
	i=i+1
vetor=zeros(j,dtype=float)
i=0
k=0
while(i<size(vet)):
	if(vet[i]<=maxi):
		vetor[k]=vetor[k]+vet[i]
		k=k+1
	i=i+1
print(vetor)

		