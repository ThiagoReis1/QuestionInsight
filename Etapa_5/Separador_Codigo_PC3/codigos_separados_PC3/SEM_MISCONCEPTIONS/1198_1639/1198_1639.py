from numpy import *
vetor=array(eval(input("Digite aqui o vetor:")))
minimo=10
i=0
q=0
while(i<size(vetor)):
	if(vetor[i]>minimo):
		q=q+1
	i=i+1
vet=zeros(q,dtype=float)
i=0
j=0
while(i<size(vetor)):
	if(vetor[i]>=minimo):
		vet[j]=vet[j]+vetor[i]
		j=j+1
	i=i+1
print(vet)