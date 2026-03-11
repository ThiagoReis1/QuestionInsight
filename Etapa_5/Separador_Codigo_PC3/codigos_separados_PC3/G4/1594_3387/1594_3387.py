from numpy import*

vet=array(eval(input()))
m=size(vet)
i=0
j=1
while i<m:
	vet[i]=vet[i]*j
	i=i+1
	j=j+1
vet1=sum(vet)
vet1=int(vet1)
print(vet1)
	