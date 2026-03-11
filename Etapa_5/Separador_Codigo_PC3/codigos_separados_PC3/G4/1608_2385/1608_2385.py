from numpy import*
vet=array(eval(input()))
i=0
s=0
s1=75
while(i<size(vet)):
	if(s+vet[i]>75):
		vet[i]=75-s
	s=s+vet[i]

	s1=s1-vet[i]
	i=i+1
	
print(s)