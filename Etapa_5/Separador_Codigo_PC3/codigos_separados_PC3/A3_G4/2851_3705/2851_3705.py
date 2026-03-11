from numpy import*
vet=array(eval(input()))
soma=0
i=0

while(i<size(vet)):
	for x in vet:
		if(vet[i]==99):
			vet[i]=0
		i=i+1
	i=i+1
print(sum(vet)*2)
